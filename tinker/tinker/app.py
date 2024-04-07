from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import create_engine, Session, select
from typing import List
from models import MarketData, MarketDataSchema


app = FastAPI()

# Create a database connection
engine = create_engine("sqlite:///market_data.db")

def get_db():
    with Session(engine) as session:
        yield session

# Level 2 API routes
@app.post("/v2/market_data/", response_model=MarketData)
def create_market_data_v2(market_data: MarketData, db: Session = Depends(get_db)):
    db.add(market_data)
    db.commit()
    db.refresh(market_data)
    return market_data

@app.get("/v2/market_data/{id}", response_model=MarketData)
def read_market_data_v2(id: int, db: Session = Depends(get_db)):
    market_data = db.get(MarketData, id)
    if not market_data:
        raise HTTPException(status_code=404, detail="Market data not found")
    return market_data

@app.put("/v2/market_data/{id}", response_model=MarketData)
def update_market_data_v2(id: int, market_data: MarketData, db: Session = Depends(get_db)):
    db_market_data = db.get(MarketData, id)
    if not db_market_data:
        raise HTTPException(status_code=404, detail="Market data not found")
    market_data_data = market_data.dict(exclude_unset=True)
    for key, value in market_data_data.items():
        setattr(db_market_data, key, value)
    db.add(db_market_data)
    db.commit()
    db.refresh(db_market_data)
    return db_market_data

@app.delete("/v2/market_data/{id}")
def delete_market_data_v2(id: int, db: Session = Depends(get_db)):
    market_data = db.get(MarketData, id)
    if not market_data:
        raise HTTPException(status_code=404, detail="Market data not found")
    db.delete(market_data)
    db.commit()
    return {"message": "Market data deleted successfully"}

@app.get("/v2/market_data/", response_model=List[MarketData])
def read_market_data_list_v2(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    market_data_list = db.exec(select(MarketData).offset(skip).limit(limit)).all()
    return market_data_list
