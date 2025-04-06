from .sntj_client import SNTJClient
from .sntj_config import SNTJConfig
from sntj.schemas import Symbol

def test_health_check(): 
    """Tests health check from SDK"""
    config = SNTJConfig(sntj_base_url="http://0.0.0.0:8000",backoff=False)
    client = SNTJClient(config)    
    response = client.get_health_check()
    assert response.status_code == 200
    assert response.json() == {"message": "API health check successful!"}

def test_get_symbols(): 
    """Tests get leagues from SDK"""
    config = SNTJConfig(sntj_base_url="http://0.0.0.0:8000",backoff=False)
    client = SNTJClient(config)    
    symbols_response = client.get_symbols(skip=0, limit=100)
    # Assert the endpoint returned a list object
    assert isinstance(symbols_response, list)
    # Assert each item in the list is an instance of a Pydantic League object
    for symbol in symbols_response:
        assert isinstance(symbol, Symbol)
    # Asset that 5 League objects are returned
    assert len(symbols_response) == 5

