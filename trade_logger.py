import json

class TradeLogger:
    def __init__(self, filename='trade_history.json'):
        self.filename = filename

    def log_trade(self, trade_data):
        """
        Logs a trade to the JSON file.
        :param trade_data: Dictionary containing trade details.
        """
        trade_data['timestamp'] = self.get_current_time()
        try:
            with open(self.filename, 'a') as f:
                json.dump(trade_data, f)
                f.write('\n')
        except Exception as e:
            print(f'Error logging trade: {e}')

    def retrieve_trade_history(self):
        """
        Retrieves the trade history from the JSON file.
        :return: List of trade records.
        """
        try:
            with open(self.filename, 'r') as f:
                return [json.loads(line) for line in f if line.strip()]
        except FileNotFoundError:
            return []  # Return empty list if file doesn't exist
        except Exception as e:
            print(f'Error retrieving trade history: {e}')
            return []

    @staticmethod
    def get_current_time():
        from datetime import datetime
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
