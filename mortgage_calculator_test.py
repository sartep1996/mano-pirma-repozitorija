import unittest
from mortgage_calculator import MortgageCalculator

class TestMortgageCalculator(unittest.TestCase):
    def setUp(self):
        self.obj = MortgageCalculator(1000, 5, 5 )


    def test_interest_rate(self):
        calculator = MortgageCalculator(1000000, 4, 30)
        calculator.monthly_interest_rate(5)
        self.assertEqual(calculator.monthly_interest_rate, 0.0035)
    
    def test_increased_interest_rate(self):
        calculator = MortgageCalculator(1000000, 4, 30)
        calculator.increased_interest_rate(3)
        self.assertEqual(calculator.monthly_interest_rate, 0.0025)

    def test_payment_schedule(self):
        calculator = MortgageCalculator(1000000, 4, 30)
        schedule = calculator.payment_schedule()
        self.assertEqual(len(schedule), 360)
        self.assertAlmostEqual(schedule[0]["principal"], 2777.78, places=2)
        self.assertAlmostEqual(schedule[0]['interest'], 3333.33, places=2)

if __name__ == "__main__":
    unittest.main()