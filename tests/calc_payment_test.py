import unittest
from calc_payment.calc_payment_model import CalcPayment
from calc_payment import calc_payment_exceptions


class TestCalcPayment(unittest.TestCase):

    def test_monthly_payment(self):
        amount: float = 200000
        interest_rate: float = 3.1
        number_of_payments: int = 36
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result: float = round(calc.calc_monthly_payment(), 2)
        expected_result: float = 9297.96
        self.assertEqual(result, expected_result)

    def test_total_interest(self):
        amount: float = 200000
        interest_rate: float = 3.1
        number_of_payments: int = 36
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result: float = round(calc.calc_total_interest(),2)
        expected_result: float = 134726.53
        self.assertEqual(result, expected_result)

    def test_total_interest_2(self):
        amount: float = 850000
        interest_rate: float = 3.4
        number_of_payments: int = 24
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result: float = round(calc.calc_total_interest(),2)
        expected_result: float = 407059.97
        self.assertEqual(result, expected_result)

    def test_interest(self):
        amount: float = 480000
        interest_rate: float = 0
        number_of_payments: int = 48
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result: float = round(calc.calc_total_interest(), 2)
        expected_result: float = 0
        self.assertEqual(result, expected_result)

    def test_usury(self):
        amount: float = 50000
        interest_rate: float = 12.4
        number_of_payments: int = 48
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(calc_payment_exceptions.Usury, calc.calc_monthly_payment)

    def test_single_payment(self):
        amount: float = 90000
        interest_rate: float = 2.4
        number_of_payments: int = 1
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result: float = round(calc.calc_total_interest(), 2)
        expected_result: float = 0
        self.assertEqual(result, expected_result)

    def test_zero_amount(self):
        amount: float = 0
        interest_rate: float = 2.4
        number_of_payments: int = 60
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(calc_payment_exceptions.ZeroAmount, calc.calc_monthly_payment)

    def test_negative_number_of_payments(self):
        amount: float = 2
        interest_rate: float = 3.1
        number_of_payments: int = -2
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(calc_payment_exceptions.NegativeNumberOfPayments, calc.calc_monthly_payment)

    def test_amortization(self):
        amount: float = 200000
        interest_rate: float = 3.10
        number_of_payments: int = 36
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table: list = calc.amortization()
        self.assertListEqual(table, [[1, 196902.04, 6200.0, 3097.96], [2, 193708.04, 6103.96, 3194.0], [3, 190415.03, 6004.95, 3293.01], [4, 187019.94, 5902.87, 3395.09], [5, 183519.6, 5797.62, 3500.34], [6, 179910.75, 5689.11, 3608.85], [7, 176190.02, 5577.23, 3720.73], [8, 172353.95, 5461.89, 3836.07], [9, 168398.96, 5342.97, 3954.99], [10, 164321.37, 5220.37, 4077.59], [11, 160117.37, 5093.96, 4204.0], [12, 155783.05, 4963.64, 4334.32], [13, 151314.36, 4829.27, 4468.69], [14, 146707.15, 4690.75, 4607.21], [15, 141957.11, 4547.92, 4750.04], [16, 137059.82, 4400.67, 4897.29], [17, 132010.71, 4248.85, 5049.11], [18, 126805.08, 4092.33, 5205.63], [19, 121438.08, 3930.96, 5367.0], [20, 115904.7, 3764.58, 5533.38], [21, 110199.79, 3593.05, 5704.91], [22, 104318.02, 3416.19, 5881.77], [23, 98253.92, 3233.86, 6064.1], [24, 92001.83, 3045.87, 6252.09], [25, 85555.93, 2852.06, 6445.9], [26, 78910.2, 2652.23, 6645.73], [27, 72058.46, 2446.22, 6851.74], [28, 64994.31, 2233.81, 7064.15], [29, 57711.17, 2014.82, 7283.14], [30, 50202.26, 1789.05, 7508.91], [31, 42460.57, 1556.27, 7741.69], [32, 34478.89, 1316.28, 7981.68], [33, 26249.78, 1068.85, 8229.11], [34, 17765.56, 813.74, 8484.22], [35, 9018.33, 550.73, 8747.23], [36, 0, 279.57, 9018.39]])

    def test_amortization_2(self):
        amount: float = 850000
        interest_rate: float = 3.40
        number_of_payments: int = 24
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table: list = calc.amortization()
        self.assertListEqual(table, [[1, 826522.5, 28900.0, 23477.5], [2, 802246.77, 28101.77, 24275.73], [3, 777145.66, 27276.39, 25101.11], [4, 751191.11, 26422.95, 25954.55], [5, 724354.11, 25540.5, 26837.0], [6, 696604.65, 24628.04, 27749.46], [7, 667911.71, 23684.56, 28692.94], [8, 638243.21, 22709.0, 29668.5], [9, 607565.98, 21700.27, 30677.23], [10, 575845.72, 20657.24, 31720.26], [11, 543046.97, 19578.75, 32798.75], [12, 509133.07, 18463.6, 33913.9], [13, 474066.09, 17310.52, 35066.98], [14, 437806.84, 16118.25, 36259.25], [15, 400314.77, 14885.43, 37492.07], [16, 361547.97, 13610.7, 38766.8], [17, 321463.1, 12292.63, 40084.87], [18, 280015.35, 10929.75, 41447.75], [19, 237158.37, 9520.52, 42856.98], [20, 192844.25, 8063.38, 44314.12], [21, 147023.45, 6556.7, 45820.8], [22, 99644.75, 4998.8, 47378.7], [23, 50655.17, 3387.92, 48989.58], [24, 0, 1722.28, 50655.22]]
)

    def test_amortization_single_payment(self):
        amount: float = 90000
        interest_rate: float = 2.40
        number_of_payments: int = 1
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table: list = calc.amortization()
        self.assertListEqual(table, [[1, 0, 0, 90000]])

    def test_amortization_zero_interest_rate(self):
        amount: float = 480000
        interest_rate: float = 0
        number_of_payments: int = 48
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table: list = calc.amortization()
        self.assertListEqual(table, [[1, 470000.0, 0.0, 10000.0], [2, 460000.0, 0.0, 10000.0], [3, 450000.0, 0.0, 10000.0], [4, 440000.0, 0.0, 10000.0], [5, 430000.0, 0.0, 10000.0], [6, 420000.0, 0.0, 10000.0], [7, 410000.0, 0.0, 10000.0], [8, 400000.0, 0.0, 10000.0], [9, 390000.0, 0.0, 10000.0], [10, 380000.0, 0.0, 10000.0], [11, 370000.0, 0.0, 10000.0], [12, 360000.0, 0.0, 10000.0], [13, 350000.0, 0.0, 10000.0], [14, 340000.0, 0.0, 10000.0], [15, 330000.0, 0.0, 10000.0], [16, 320000.0, 0.0, 10000.0], [17, 310000.0, 0.0, 10000.0], [18, 300000.0, 0.0, 10000.0], [19, 290000.0, 0.0, 10000.0], [20, 280000.0, 0.0, 10000.0], [21, 270000.0, 0.0, 10000.0], [22, 260000.0, 0.0, 10000.0], [23, 250000.0, 0.0, 10000.0], [24, 240000.0, 0.0, 10000.0], [25, 230000.0, 0.0, 10000.0], [26, 220000.0, 0.0, 10000.0], [27, 210000.0, 0.0, 10000.0], [28, 200000.0, 0.0, 10000.0], [29, 190000.0, 0.0, 10000.0], [30, 180000.0, 0.0, 10000.0], [31, 170000.0, 0.0, 10000.0], [32, 160000.0, 0.0, 10000.0], [33, 150000.0, 0.0, 10000.0], [34, 140000.0, 0.0, 10000.0], [35, 130000.0, 0.0, 10000.0], [36, 120000.0, 0.0, 10000.0], [37, 110000.0, 0.0, 10000.0], [38, 100000.0, 0.0, 10000.0], [39, 90000.0, 0.0, 10000.0], [40, 80000.0, 0.0, 10000.0], [41, 70000.0, 0.0, 10000.0], [42, 60000.0, 0.0, 10000.0], [43, 50000.0, 0.0, 10000.0], [44, 40000.0, 0.0, 10000.0], [45, 30000.0, 0.0, 10000.0], [46, 20000.0, 0.0, 10000.0], [47, 10000.0, 0.0, 10000.0], [48, 0.0, 0.0, 10000.0]]
)

    def test_amortization_extra_payment(self):
        amount: float = 200000
        interest_rate: float = 3.10
        number_of_payments: int = 36
        period: int = 10
        extra_payment: float = 53000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = calc.calc_extra_payment(extra_payment, period)
        self.assertListEqual(result, [[1, 196902.04, 6200.0, 3097.96], [2, 193708.04, 6103.96, 3194.0], [3, 190415.03, 6004.95, 3293.01], [4, 187019.94, 5902.87, 3395.09], [5, 183519.6, 5797.62, 3500.34], [6, 179910.75, 5689.11, 3608.85], [7, 176190.02, 5577.23, 3720.73], [8, 172353.95, 5461.89, 3836.07], [9, 168398.96, 5342.97, 3954.99], [10, 120619.33, 5220.37, 47779.63], [11, 115060.57, 3739.2, 5558.76], [12, 109329.49, 3566.88, 5731.08], [13, 103420.74, 3389.21, 5908.75], [14, 97328.82, 3206.04, 6091.92], [15, 91048.05, 3017.19, 6280.77], [16, 84572.58, 2822.49, 6475.47], [17, 77896.37, 2621.75, 6676.21], [18, 71013.2, 2414.79, 6883.17], [19, 63916.65, 2201.41, 7096.55], [20, 56600.11, 1981.42, 7316.54], [21, 49056.75, 1754.6, 7543.36], [22, 41279.55, 1520.76, 7777.2], [23, 33261.26, 1279.67, 8018.29], [24, 24994.4, 1031.1, 8266.86], [25, 16471.27, 774.83, 8523.13], [26, 7683.92, 510.61, 8787.35], [27, 0, 238.2, 7683.92]]
)

    def test_amortization_extra_payment_2(self):
        amount: float = 850000
        interest_rate: float = 3.40
        number_of_payments: int = 24
        payment_number: int = 5
        extra_payment: float = 90000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result: list = calc.calc_extra_payment(extra_payment, payment_number)
        self.assertListEqual(result, [[1, 826522.5, 28900.0, 23477.5], [2, 802246.77, 28101.77, 24275.73], [3, 777145.66, 27276.39, 25101.11], [4, 751191.11, 26422.95, 25954.55], [5, 686731.61, 25540.5, 64459.5], [6, 657702.98, 23348.87, 29028.63], [7, 627687.38, 22361.9, 30015.6], [8, 596651.25, 21341.37, 31036.13], [9, 564559.89, 20286.14, 32091.36], [10, 531377.43, 19195.04, 33182.46], [11, 497066.76, 18066.83, 34310.67], [12, 461589.53, 16900.27, 35477.23], [13, 424906.07, 15694.04, 36683.46], [14, 386975.38, 14446.81, 37930.69], [15, 347755.04, 13157.16, 39220.34], [16, 307201.21, 11823.67, 40553.83], [17, 265268.55, 10444.84, 41932.66], [18, 221910.18, 9019.13, 43358.37], [19, 177077.63, 7544.95, 44832.55], [20, 130720.77, 6020.64, 46356.86], [21, 82787.78, 4444.51, 47932.99], [22, 33225.06, 2814.78, 49562.72], [23, 0, 1129.65, 33225.06]]
)

    def test_amortization_insufficient_extra_payment(self):
        amount: float = 850000
        interest_rate: float = 3.40
        number_of_payments: int = 24
        payment_number: int = 10
        extra_payment: float = 45000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(calc_payment_exceptions.InsufficientPayment, calc.calc_extra_payment, extra_payment, payment_number)

    def test_amortization_greater_extra_payment(self):
        amount: float = 850000
        interest_rate: float = 3.40
        number_of_payments: int = 24
        payment_number: int = 22
        extra_payment: float = 180000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(calc_payment_exceptions.GreaterPayment, calc.calc_extra_payment, extra_payment, payment_number)
