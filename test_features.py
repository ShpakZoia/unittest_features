import unittest
from my_atm.features import *

class TestAtm(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.atm_balance = 10000
        self.client_can_get_money = True

    def test_rise_money(self):
        self.assertEqual(self.atm.rise_money(200), 10200)

    def test_rise_money_negative(self):
        self.assertEqual(self.atm.rise_money("%%%%"), 10000)

    def test_get_money(self):
        self.assertEqual(self.atm.get_money(5000), 5000)

    def test_get_money_negativ(self):
        self.assertEqual(self.atm.get_money(10001), 10000)

    def test_get_money_zero(self):
        self.assertEqual(self.atm.get_money(0), 10000)

    def test_get_money_minus(self):
        self.assertEqual(self.atm.get_money(-1), 10000)

    def test_check_balance(self):
        self.assertEqual(self.atm_balance, 10000)

    def test_incorrect_balance(self):
        self.assertEqual(self.atm_balance, 9000)


if __name__ == '__main__':
    unittest.main()
