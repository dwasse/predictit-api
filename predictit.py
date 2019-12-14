import requests

URL = "https://www.predictit.org/api/"

class Predictit:

    def __init__(self):
        pass

    def _parse_response(self, response):
        if response.status_code == 200:
            return response.json()
        raise Exception("Bad response from predictit API: " + str(response.status_code))

    def get_all_markets(self):
        response = requests.get(URL + "marketdata/all/").json()
        return self._parse_response(response)

    def get_market_data(self, market_id):
        response = requests.get(URL + "marketdata/markets/" + str(market_id))
        return self._parse_response(response)

    def get_contract_data(self, market_id, contract_id):
        market_data = self.get_market_data(market_id)
        if len(market_data['contracts']) > 1 and contract_id is None:
            raise Exception("Did not pass contract_id to categorical market!")
        contract_index = None
        if contract_id is None:
            contract_index = 0
        else:
            count = 0
            for contract in market_data['contracts']:
                if contract['id'] == contract_id:
                    contract_index = count
                    break
                else:
                    count += 1
        if contract_index is None:
            raise Exception("Could not find contract with market_id " + str(market_id) + " and contract id " + str(contract_id))
        return market_data['contracts'][contract_index]

    def get_mid_market_price(self, market_id, contract_id=None):
        contract_data = self.get_contract_data(market_id, contract_id)
        if contract_data is None:
            return
        return (contract_data['bestBuyYesCost'] + contract_data['bestSellYesCost']) / 2

    def get_last_price(self, market_id, contract_id=None):
        contract_data = self.get_contract_data(market_id, contract_id)
        if contract_data is None:
            return
        return contract_data['lastTradePrice']
        

if __name__ == "__main__":
    client = Predictit()
    market_data = client.get_all_markets()
    print(market_data)
