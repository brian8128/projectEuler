class Sieve:
  'For telling which numbers are prime and which are composite.'
  'Construction is O(nlog(log(n))), lookups constant time thereafter.'
  'Memory used is O(n)'


  def _setNotPrime(self, k):
    self.sieve[k-1] = False
    return

  def isPrime(self, k):
    return self.sieve[k-1]

  def __init__(self, n):

    # array of n booleans initalized to true
    self.sieve = [True] * n

    # 1 is not prime
    self._setNotPrime(1)

    for i in range(2, n):
      if self.isPrime(i):
        tmp = 2 * i
        while tmp <= n:
          self._setNotPrime(tmp)
          tmp += i
