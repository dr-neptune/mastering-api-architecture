import requests
from pactman import Consumer, Provider

pact = Consumer('MarketDataConsumer').has_pact_with(Provider('MarketDataAPI'))

# @pact.given('a market data entry exists with ID 1')
def test_get_market_data_by_id():
    market_data_id = 1

    expected_response = {
        'id': market_data_id,
        'Date': '2022-01-04T00:00:00',
        'Open': 182.630004882812,
        'High': 182.940002441406,
        'Low': 179.119995117188,
        'Close': 179.699996948242,
        'Adj_Close': 177.443557739258,
        'Volume': 99310400.0,
        'Symbol': 'AAPL'
    }

    (pact
     .given('a market data entry exists with ID 1')
     .upon_receiving('a request for market data with ID 1')
     .with_request(
         method='GET',
         path=f'http://localhost:8000/market_data/{market_data_id}',
     )
     .will_respond_with(
         status=200,
         body=expected_response
     ))

    with pact:
        result = requests.get(f'/market_data/{market_data_id}').json()
        assert result == expected_response
