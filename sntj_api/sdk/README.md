# sntj software development kit (SDK)
This is the Python SDK to interact with the financial data, 

## Installing sntj

To install this SDK in your environment, execute the following command:



## Example usage

This SDK implements all the endpoints in the SNTJ API, 

### Setting base URL for the API
The SDK looks for a value of `SNTJ_API_BASE_URL` in the environment. The preferred 
method for setting the base URL for the SNTJ API is by creating a Python 
`.env` file in your project directory with the following value:

```
SNTJ_API_BASE_URL={URL of your API}
```

You may also set this value as an environment variable in the environment you 
are using the SDK, or pass it as a parameter to the `SNTJConfig()` method.


### Example of normal API functions

To call the SDK functions for normal API endpoints, here is an example:

```python
from sntj import SNTJClient
from sntj import SNTJConfig

config = SNTJConfig(sntj_base_url="http://0.0.0.0:8000",backoff=False)
client = SNTJClient(config)    
symbol = client.symbol()
print(symbol)
```

