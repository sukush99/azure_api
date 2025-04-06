import httpx
import sntj.sntj_config as config
from .schemas import Symbol, BalanceSheet
from typing import List
import backoff
from loguru import logger

class SNTJClient:
    """
    Interacts with the SNTJ API to fetch data.

    This SDK class simplifies the process of using the SNTJ API by providing methods to fetch

    Typical usage example:
         client = SNTJClient()
         response = client.get_symbol
    """

    HEATH_CHECK_ENDPOINT = "/"
    SYMBOLS_ENDPOINT = "/v0/symbols/"
    BALANCE_SHEET_ENDPOINT = "/v0/balance_sheet/{symbol}/"

    #BULK_FILE_BASE_URL = ""
    
    def __init__(self, input_config: config.SNTJConfig):
        """
        Initialize the SNTJClient with the provided configuration.

        Args:
            input_config (SNTJConfig): Configuration object for SNTJ API.

        Returns:
            None
        """

        logger.debug("Initializing SNTJClient with configuration: {}", input_config)
        if not isinstance(input_config, config.SNTJConfig):
            raise ValueError("input_config must be an instance of SNTJConfig")
        self.sntj_base_url = input_config.sntj_base_url
        self.backoff = input_config.sntj_backoff
        self.ackoff_max_time = input_config.sntj_backoff_max_time
        self.bulk_file_format = input_config.sntj_bulk_file_format

        if self.backoff:
            logger.debug("Backoff is enabled with max time: {}", self.backoff_max_time)
            self.call_api = backoff.on_exception(
                wait_gen=backoff.expo,
                exception=(httpx.HTTPStatusError,httpx.HTTPStatusError),
                max_time=self.backoff_max_time,
                jitter=backoff.random_jitter,
            )(self.call_api)

    
    def call_api(self,api_endpoint: str,api_params: dict = None) -> httpx.Response:
        """Call the SNTJ API with the specified endpoint and parameters.
        Args:
            api_endpoint (str): API endpoint to call.
            api_params (dict): Parameters for the API call.
        Returns:
            httpx.Response: Response object from the API call.
        """

        # logger.debug("Calling API endpoint: {}", api_endpoint)
        # logger.debug("API parameters: {}", api_params)

        if api_params:
            api_params = {key: val for key, val in api_params.items() if val is not None}

        try:
            with httpx.Client(base_url=self.sntj_base_url) as client:
                #logger.debug("Making GET request to {} with params: {}", api_endpoint, api_params)
                response = client.get(api_endpoint, params=api_params)
                logger
                return response
        except httpx.RequestError as exc:
            logger.error(f"An error occurred while requesting {exc.request.url}: {exc}")
            raise
        except httpx.HTTPStatusError as exc:
            logger.error(f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}")
            raise
        
                
    def get_health_check(self) -> httpx.Response:
        """
        Check the health of the SNTJ API.

        Returns:
            httpx.Response: Response object from the health check.
        """
        logger.debug("Performing health check")
        endpoint_url = self.HEATH_CHECK_ENDPOINT
        return self.call_api(endpoint_url)
    
    def get_symbols(self, skip: int = 0, limit: int = 100) -> List[Symbol]:
        """
        Get a list of symbols from the SNTJ API.

        Args:
            skip (int): Number of records to skip (default: 0).
            limit (int): Maximum number of records to return (default: 100).

        Returns:
            List[Symbol]: List of Symbol objects.
        """
        #logger.debug("Fetching symbols with skip: {}, limit: {}", skip, limit)
        endpoint_url = self.SYMBOLS_ENDPOINT
        api_params = {"skip": skip, "limit": limit}
        response = self.call_api(endpoint_url, api_params)
        
        if response.status_code == 200:
            symbols_data = response.json()
            return [Symbol(**symbol) for symbol in symbols_data]
        else:
            logger.error(f"Failed to fetch symbols: {response.status_code} - {response.text}")
            return []