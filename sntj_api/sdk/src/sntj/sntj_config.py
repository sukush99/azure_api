import os
#from dotenv import load_dotenv

class SNTJConfig:
    """
    Configuration class for SNTJ API.
    This class loads environment variables from a .env file and provides
    access to the SNTJ API base URL and other configurations.
    """

    sntj_base_url: str
    sntj_backoff: bool
    sntj_backoff_max_time: int
    sntj_bulk_file_format: str

    def __init__(self,
                 sntj_base_url: str = None,
                 backoff: bool = True,
                 backoff_max_time: int = 30,
                 bulk_file_format: str = "csv"):
        """
        Initialize the SNTJConfig class with the given parameters.
        Args:
            sntj_base_url (str): Base URL for the SNTJ API.
            backoff (bool): Enable or disable backoff strategy.
            backoff_max_time (int): Maximum time for backoff in seconds.
            bulk_file_format (str): Format for bulk file operations.
        returns:
            None
        """
        self.sntj_base_url = sntj_base_url or os.getenv("SNTJ_BASE_URL")

        if not self.sntj_base_url:
            raise ValueError("Base URL is required. Set SNTJ_BASE_URL environment variable.")

        self.sntj_backoff = backoff
        self.sntj_backoff_max_time = backoff_max_time
        self.sntj_bulk_file_format = bulk_file_format

    def __str__(self):
        """Stringify the SNTJConfig object."""
        return f"SNTJConfig(sntj_base_url={self.sntj_base_url}, backoff={self.sntj_backoff}, backoff_max_time={self.sntj_backoff_max_time}, bulk_file_format={self.sntj_bulk_file_format})"