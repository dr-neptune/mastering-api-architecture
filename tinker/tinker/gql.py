import strawberry
from sqlalchemy import create_engine, Column, Integer, DateTime, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///market_data.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the MarketData model
class MarketDataModel(Base):
    __tablename__ = 'market_data'
    id = Column(Integer, primary_key=True)
    Date = Column(DateTime)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Adj_Close = Column(Float)
    Volume = Column(Float)
    Symbol = Column(String)

# Create a GraphQL type for MarketData
@strawberry.type
class MarketData:
    id: int
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Adj_Close: float
    Volume: float
    Symbol: str

# Define the Query type
@strawberry.type
class Query:
    @strawberry.field
    def market_data_by_id(self, id: int) -> MarketData:
        market_data = session.query(MarketDataModel).filter_by(id=id).first()
        return MarketData(
            id=market_data.id,
            Date=str(market_data.Date),
            Open=market_data.Open,
            High=market_data.High,
            Low=market_data.Low,
            Close=market_data.Close,
            Adj_Close=market_data.Adj_Close,
            Volume=market_data.Volume,
            Symbol=market_data.Symbol
        )

if __name__ == '__main__':
    # Create the GraphQL schema
    schema = strawberry.Schema(query=Query)

    # Execute a sample query
    query = '''
    query {
        marketDataById(id: 1) {
            id
            Date
            Open
            High
            Low
            Close
            AdjClose
            Volume
            Symbol
        }
    }
    '''

    result = schema.execute_sync(query)
    print(result.data)
