from sqlalchemy.orm import Session
from sqlalchemy import asc, desc 
# from sqlalchemy.orm import joinedload
# from datetime import date

# mapping fo the models to the database
import models

# select top(1) * from player where player_id = {player_id}
def get_symbols(db: Session,
                skip: int = 0,
                limit: int = 100,):
    return db.query(models.DimSymbol).order_by(models.DimSymbol.symbol_id).offset(skip).limit(limit).all()

def get_balance_sheet_symbol(db: Session,
                      symbol: str,
                      skip: int = 0,
                      limit: int = 100):
    return db.query(models.BalanceSheet).filter(models.BalanceSheet.symbol == symbol).order_by(models.BalanceSheet.year.desc()).offset(skip).limit(limit).all()