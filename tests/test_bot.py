import unittest
from your_module import Config, Database, calculate_position_size

class TestConfigValues(unittest.TestCase):
    def test_valid_config(self):
        config = Config()
        self.assertTrue(config.is_valid())
        self.assertIsInstance(config.api_key, str)
        self.assertGreater(config.starting_balance, 0)

class TestDatabaseInsertion(unittest.TestCase):
    def test_insert_trade(self):
        db = Database()
        trade_data = {'symbol': 'AAPL', 'amount': 10, 'price': 150}
        result = db.insert_trade(trade_data)
        self.assertTrue(result)

class TestPositionSizeCalculation(unittest.TestCase):
    def test_calculate_position_size(self):
        balance = 1000
        risk = 0.01  # 1%
        price_per_unit = 50
        position_size = calculate_position_size(balance, risk, price_per_unit)
        self.assertEqual(position_size, 20)

if __name__ == '__main__':
    unittest.main()