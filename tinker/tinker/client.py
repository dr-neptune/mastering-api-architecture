import grpc
import market_data_pb2
import market_data_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = market_data_pb2_grpc.MarketDataServiceStub(channel)

        # Get a single market data entry by ID
        response = stub.GetMarketData(market_data_pb2.GetMarketDataRequest(id=100))
        print("Market Data:")
        print(f"ID: {response.id}")
        print(f"Date: {response.date}")
        print(f"Open: {response.open}")
        print(f"High: {response.high}")
        print(f"Low: {response.low}")
        print(f"Close: {response.close}")
        print(f"Adj Close: {response.adj_close}")
        print(f"Volume: {response.volume}")
        print(f"Symbol: {response.symbol}")

        # Get a list of market data entries
        print("\nMarket Data List:")
        for response in stub.ListMarketData(market_data_pb2.ListMarketDataRequest(limit=15)):
            print(f"ID: {response.id}, Date: {response.date}, Symbol: {response.symbol}")

if __name__ == '__main__':
    run()
