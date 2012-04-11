__author__ = '@PavelVavruska'


class PrimeChecker:
    prime_numbers = [0, 1, 2, 3]

    @staticmethod
    def isPrimeNumber(number):
        if number in PrimeChecker.prime_numbers:
            return True
        # Even numbers are not prime numbers
        if number % 2 == 0:
            return 2
        # Searching in odd numbers 3, 5, 7, ...
        for x in xrange(3, number - 1, 2):
            if number % x == 0:
                return x
        return True
