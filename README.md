cat README.md
# SNTJ API: Financial Data API

## Overview
SNTJ API is a FastAPI-based REST service that provides read-only access to stock and financial data hosted on Azure SQL Database. The API offers comprehensive endpoints for accessing financial statements, stock symbols, and market data.

## Features
- **Financial Data Access**: Retrieve detailed financial information including:
  - Balance Sheets
  - Income Statements
  - Cash Flow Statements
  - Statement of Operations
- **Market Data**:
  - OHLC (Open, High, Low, Close) daily price data
  - Technical indicators (SMA, EMA, RSI, MACD, etc.)
- **Reference Data**:
  - Company symbols
  - Exchange information
  - Timestamps and historical data

## Technical Stack
- **Python**: >=3.11
- **Framework**: FastAPI v0.115.0+
- **Database**: Azure SQL Database (via pyodbc)
- **Authentication**: Azure Identity
- **Container Support**: Docker with SQL Server drivers

### Key Dependencies
- SQLAlchemy (>=2.0.0): Database ORM
- Pydantic (>=2.4.0): Data validation
- FastAPI: Web framework
- Azure Identity: Authentication
- PyODBC: SQL Server connectivity
- Uvicorn: ASGI server

## Project Structure
```
sntj_api/
├── main.py           # FastAPI application and routes
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic models for API
├── crud.py           # Database operations
├── database.py       # Database connection setup
├── azure_config.py   # Azure configuration
└── sdk/              # Client SDK package
```

## API Endpoints
- `/` - Health check endpoint
- `/v0/symbols/` - List all available symbols
- `/v0/exchanges/` - List all exchanges
- `/v0/timestamps/` - Retrieve timestamp information
- `/v0/cash_flow/{symbol}/` - Cash flow statements by symbol
- `/v0/income_statement/{symbol}/` - Income statements by symbol
- `/v0/balance_sheet/{symbol}/` - Balance sheets by symbol
- `/v0/statement_operation/{symbol}/` - Operational statements by symbol
- `/v0/ohlc/{symbol}/` - OHLC price data by symbol

## Data Models
The API includes comprehensive models for:
- **DimSymbol**: Symbol reference data (CIK, ISIN, CUSIP, etc.)
- **BalanceSheet**: Detailed balance sheet data with over 100 financial metrics
- **CashFlow**: Cash flow statement data including operating, investing, and financing activities
- **IncomeStatement**: Income statement data with comprehensive income metrics
- **StatementOperation**: Operational financial data including earnings per share and revenue
- **OHLCDaily**: Market data with price information and numerous technical indicators
- **DimExchange**: Exchange reference data
- **DimTimestamp**: Time reference data

## Setup and Installation

### Prerequisites
- Python 3.11 or higher
- SQL Server ODBC drivers (included in Docker setup)
- Access to Azure SQL Database

### Local Development
1. Clone the repository
   ```bash
   git clone <repository-url>
   cd sntj_api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in azure_conn.env:
   ```
   # Example configuration
   AZURE_SQL_SERVER=your-server.database.windows.net
   AZURE_SQL_DATABASE=your-database
   AZURE_SQL_USERNAME=your-username
   AZURE_SQL_PASSWORD=your-password
   ```

4. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation at:
   ```
   http://localhost:8000/docs
   ```

### Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t sntj-api .
   ```

2. Run the container:
   ```bash
   docker run -p 80:80 --env-file azure_conn.env sntj-api
   ```

3. Access the API at:
   ```
   http://localhost/docs
   ```

## Development Tools
- **Ruff**: Code linting and formatting
- **Pytest**: Testing framework
- **Makefile**: Build and development automation

## Testing
Run tests using pytest:
```bash
pytest test_crud.py test_main.py
```

## SDK Usage
The Python client SDK in the `/sdk` directory provides easy API integration:

```python
from sntj.sntj_client import SNTJClient

# Create a client
client = SNTJClient(base_url="http://localhost:8000")

# Get symbols
symbols = client.get_symbols()

# Get balance sheet for a specific symbol
balance_sheets = client.get_balance_sheets("AAPL")
```

## Authentication
The API uses Azure Identity for authentication to the database. The API endpoints themselves do not require authentication, but it's recommended to secure the API in production environments.

## Error Handling
The API returns standard HTTP status codes:
- `200 OK`: Request successful
- `400 Bad Request`: Invalid request
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server-side error

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
[License information not specified in the codebase]

## Version
Current version: 0.1.0



#### Document
- https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com/redoc
- https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com/docs


