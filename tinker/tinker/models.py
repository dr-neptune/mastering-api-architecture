from sqlmodel import SQLModel, Field
from typing import Optional

class MarketData(SQLModel, table=True):
    __tablename__ = 'market_data'

    id: Optional[int] = Field(default=None, primary_key=True)
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Adj_Close: float
    Volume: float
    Symbol: str
