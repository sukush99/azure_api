from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#test the health check endpoint
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API health check successful!"}

#test /v0/symbols/ endpoint
def test_read_symbols():
    response = client.get("/v0/symbols/?skip=0&limit=100")
    assert response.status_code == 200
    assert len(response.json()) == 5

#test /v0/balance_sheet/{symbol}/ endpoint
def test_read_balance_sheet_symbol():
    symbol = "AAPL"
    response = client.get(f"/v0/balance_sheet/{symbol}/?skip=0&limit=100")
    assert response.status_code == 200
    #assert len(response.json()) == 5

