import backtrader as bt
import datetime
import yfinance as yf

class MyStrategy(bt.Strategy):
    # Define the parameters for the strategy
    params = (('sma_period', 15),)

    def __init__(self):
        # Simple Moving Average
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_period)

    def next(self):
        if self.data.close[0] > self.sma[0]:  # If the close price is greater than SM
            if not self.position:  # If not in the market
                self.buy()  # Enter long
        elif self.data.close[0] < self.sma[0]:  # Close price less than SM
            if self.position:  # If in the market
                self.sell()  # Exit position

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MyStrategy)

    # Downloading Yahoo Finance data
    data = bt.feeds.PandasData(dataname=yf.download('AAPL', start='2024-01-01', end='2026-04-05'))
    cerebro.adddata(data)

    cerebro.run()  # Execute the strategy
    cerebro.plot()  # Plot the results
