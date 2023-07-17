from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide,TimeInForce
from alpaca.trading.requests import MarketOrderRequest 
from alpaca.trading.stream import TradingStream

import config 

client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)

account_info = dict(client.get_account())
for key, value in account_info.items():
    print(f"{key:30}, {value}")


order_details = MarketOrderRequest(
    symbol="SPY",
    qty=100,
    side=OrderSide.BUY,
    time_in_force = TimeInForce.DAY
)

# ORDER= client.submit_order(order_data=order_details)

# trades = TradingStream(config.API_KEY, config.SECRET_KEY, paper=True)

# async def trade_status(data):
#     print(data)

# trades.subscribe_trade_updates(trade_status)
# trades.run()

assets = [assets for asset in client.get_all_positions()]
