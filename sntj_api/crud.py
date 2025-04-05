from sqlalchemy.orm import Session
# from sqlalchemy.orm import joinedload
# from datetime import date

# mapping fo the models to the database
import models

# select top(1) * from player where player_id = {player_id}
def get_symbol(db: Session):
    return db.query(models.DimSymbol).first()