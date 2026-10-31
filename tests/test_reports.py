import unittest
from features import reports


class TestReports(unittest.TestCase):

    def test_empty_history_returns_zero(self):
        data = {"history": []}
        self.assertEqual(reports.average_balance(data), 0.0)

    def test_average_of_multiple_balances(self):
        data = {"history": [100, 200, 300]}
        self.assertEqual(reports.average_balance(data), 200.0)