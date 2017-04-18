import unittest
from app.primes import Primes


class TddPrimes(unittest.TestCase):
    def setUp(self):
        self.primes = Primes()

    def test_primes_method_raises_type_error_if_arg_is_not_int(self):
        self.assertRaises(TypeError, self.primes.primes, 10.5)
        self.assertRaises(TypeError, self.primes.primes, 'string')

    def test_primes_method_raises_value_error_if_arg_is_negative(self):
        self.assertRaises(ValueError, self.primes.primes, -10)

    def test_primes_method_returns_values_without_zero_and_one(self):
        self.assertNotIn(0, self.primes.primes(10))
        self.assertNotIn(1, self.primes.primes(10))

    def test_primes_method_returns_correctly_for_zero_and_one_inputs(self):
        self.assertEqual([], self.primes.primes(1))
        self.assertEqual([], self.primes.primes(0))

    def test_primes_method_returns_correct_result(self):
        self.assertEqual([2, 3, 5, 7], self.primes.primes(10))
        self.assertEqual([2, 3, 5], self.primes.primes(5))
        self.assertEqual([2], self.primes.primes(2))


if __name__ == '__main__':
    unittest.main()
