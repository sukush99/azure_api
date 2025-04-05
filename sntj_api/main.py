from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud
from database import SessionLocal
import schemas

api_description = """
This API provides read-only access to info from the stock and financial data db hosted on Azure.
The endpoints are designed to be simple and intuitive, allowing users to easily retrieve the information they need.

The are grouped in the following categories:
- **Balance Sheet**: Operations with balance sheets.
- **Symbol**: Operations with symbols.
- **Overall health check**: General health check of the API.
## API Endpoints
- `/symbols/`: Retrieve a list of symbols with pagination.

Comming soon:
- `/balance_sheet/{symbol_id}/`: Retrieve a list of balance sheets for a specific symbol with pagination.
- `/balance_sheet/{symbol_id}/{year}/`: Retrieve a specific balance sheet for a specific symbol and year.

## Authentication
This API does not require authentication, but it is recommended to use it in a secure environment.
## Rate Limiting
This API does not have rate limiting, but it is recommended to use it in a responsible manner.
## Error Handling
This API returns standard HTTP status codes to indicate the success or failure of requests.
- `200 OK`: The request was successful.
- `400 Bad Request`: The request was invalid or cannot be served.
- `404 Not Found`: The requested resource was not found.
- `500 Internal Server Error`: An error occurred on the server side.
## Example
### Get a list of symbols
```bash
curl -X GET "http://localhost:8000/symbols/?skip=0&limit=100"
```


"""

app = FastAPI(
    title="SNTJ API: API from stock and financial data",
    description=api_description,
    version="0.1.0",
    openapi_tags=[
        {
            "name": "balance_sheet",
            "description": "Operations with balance sheets.",
        },
        {
            "name": "symbol",
            "description": "Operations with symbols.",
        },
    ],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Overall health check"],
          summary="General health check",
          description="Returns a simple message to check if the API is running.",
          response_description="API health check message",
          operation_id="health_check")
async def root():
    return {"message": "API health check successful!"}


@app.get("/v0/symbols/", tags=["symbol"],
        summary="Get lists of all the symbols in dim_symbol",
        description="Retrieve a list of symbols with pagination.",
        response_model=list[schemas.Symbol],
        response_description="List of symbols",
        operation_id="read_symbols")
def read_symbols(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=100),
    db: Session = Depends(get_db),
):
    symbols = crud.get_symbols(db, skip=skip, limit=limit)
    return symbols


@app.get("/v0/balance_sheet/{symbol}/", tags=["balance_sheet"],
        summary="Get lists of all the balance sheets for a specific symbol",
        description="Retrieve a list of balance sheets for a specific symbol with pagination.",
        response_model=list[schemas.BalanceSheet],
        response_description="List of balance sheets",
        operation_id="read_balance_sheet_symbol")
def read_balance_sheet_symbol(
    symbol: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=100),
    db: Session = Depends(get_db),
):
    balance_sheets = crud.get_balance_sheet_symbol(db, symbol=symbol, skip=skip, limit=limit)
    if not balance_sheets:
        raise HTTPException(status_code=404, detail="Balance sheets not found")
    return balance_sheets