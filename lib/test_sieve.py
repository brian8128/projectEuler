import nose.tools as n
from sieve import Sieve

# To run: nosetests test_sieve.py

def test_sieve():
    s = Sieve(100)
    n.assert_equal(s.isPrime(0), False)
    n.assert_equal(s.isPrime(1), False)
    n.assert_equal(s.isPrime(9), False)
    n.assert_equal(s.isPrime(2), True)
    n.assert_equal(s.isPrime(7), True)
    n.assert_equal(s.isPrime(97), True)
    n.assert_equal(s.isPrime(99), False)
