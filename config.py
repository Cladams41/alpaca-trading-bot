CONFIG = {
    'symbol': 'AAPL',
    'buy_threshold': 20,
    'sell_threshold': 30,
    'max_position_size': 100,
    'risk_per_trade': 0.02,
    'base_url': 'https://paper-api.alpaca.markets',
    'market_hours': {
        'open': '09:30',
        'close': '16:00'
    }
}

BACKTEST_CONFIG = {
    'start_date': '2024-01-01',
    'end_date': '2026-04-05',
    'initial_cash': 10000,
    'commission': 0.001,
}