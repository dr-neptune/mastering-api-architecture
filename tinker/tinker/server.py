from concurrent import futures
import grpc
import market_data_pb2
import market_data_pb2_grpc
from sqlmodel import SQLModel, Field, create_engine, Session, select


class MarketData(SQLModel, table=True):
    __tablename__ = 'market_data'

    id: int = Field(default=None, primary_key=True)
    Date: str
    Open: float
    High: float
    Low: float
    Close: float
    Adj_Close: float
    Volume: float
    Symbol: str


class MarketDataServicer(market_data_pb2_grpc.MarketDataServiceServicer):
    def __init__(self):
        self.engine = create_engine("sqlite:///market_data.db")

    def GetMarketData(self, request, context):
        with Session(self.engine) as session:
            market_data = session.get(MarketData, request.id)
            if not market_data:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Market data not found")
                return market_data_pb2.MarketData()
            return market_data_pb2.MarketData(
                id=market_data.id,
                date=market_data.Date,
                open=market_data.Open,
                high=market_data.High,
                low=market_data.Low,
                close=market_data.Close,
                adj_close=market_data.Adj_Close,
                volume=market_data.Volume,
                symbol=market_data.Symbol
            )

    def ListMarketData(self, request, context):
        with Session(self.engine) as session:
            market_data_list = session.exec(select(MarketData).limit(request.limit)).all()
            for market_data in market_data_list:
                yield market_data_pb2.MarketData(
                    id=market_data.id,
                    date=market_data.Date,
                    open=market_data.Open,
                    high=market_data.High,
                    low=market_data.Low,
                    close=market_data.Close,
                    adj_close=market_data.Adj_Close,
                    volume=market_data.Volume,
                    symbol=market_data.Symbol
                )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_data_pb2_grpc.add_MarketDataServiceServicer_to_server(MarketDataServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
