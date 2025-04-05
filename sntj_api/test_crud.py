import pytest

import crud
from database import SessionLocal

@pytest.fixture(scope="function")
def db_session():
    """Create a new database session for a test."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_get_symbol(db_session):
    """Test that the first symbol we get is AAPL"""
    symbol = crud.get_symbol(db_session)
    assert symbol.symbol_id == "AAPL"


