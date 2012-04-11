__author__ = '@PavelVavruska'

import unittest

from ..src.prime_checker import PrimeChecker


class TestPrimeChecker(unittest.TestCase):
    def test_prime_numbers(self):

        self.assertEqual(PrimeChecker.isPrimeNumber(1), True)

        self.assertEqual(PrimeChecker.isPrimeNumber(3), True)

        self.assertEqual(PrimeChecker.isPrimeNumber(9), 3)

        self.assertEqual(PrimeChecker.isPrimeNumber(15), 3)

        self.assertEqual(PrimeChecker.isPrimeNumber(99), 3)

        self.assertEqual(PrimeChecker.isPrimeNumber(101), True)

if __name__ == '__main__':
    unittest.main()
