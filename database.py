import sqlite3

class TradeDB:
    def __init__(self, db_name='trades.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        # Create trades table
        self.connection.execute('''CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY,
            symbol TEXT,
            trade_type TEXT,
            quantity REAL,
            price REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )')

        # Create performance metrics table
        self.connection.execute('''CREATE TABLE IF NOT EXISTS performance (
            id INTEGER PRIMARY KEY,
            total_trades INTEGER,
            total_profit REAL,
            avg_trade_duration REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )')

    def insert_trade(self, symbol, trade_type, quantity, price):
        self.connection.execute('''INSERT INTO trades (symbol, trade_type, quantity, price)
            VALUES (?, ?, ?, ?)''', (symbol, trade_type, quantity, price))
        self.connection.commit()

    def get_all_trades(self):
        return self.connection.execute('SELECT * FROM trades').fetchall()

    def __del__(self):
        self.connection.close()