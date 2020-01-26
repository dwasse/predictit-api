## PredictIt Python API

This is a minimalistic Python API wrapper for PredictIt. It supports pulling market data via HTTP GET requests.

## Getting Started

To view data from all markets, run `python3 predictit.py`.

If you would like to use the API client in a different Python module, import the client and instantiate it:

```
from predictit-api import Predictit

client = Predictit()
```

Then, you can call an API method:

```
market_data = client.get_all_markets()
```
