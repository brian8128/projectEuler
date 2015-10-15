class Sieve:
  'For telling which numbers are prime and which are composite.'
  'Construction is O(nlog(log(n))), lookups constant time thereafter.'
  'Memory used is O(n)'

  def isPrime(self, k):
    return self.sieve[k]

  def __init__(self, n):

    # array of n booleans initalized to true
    self.sieve = [True] * n

    # 0 and 1 are not prime
    self.sieve[0] = False
    self.sieve[1] = False

    for i in range(2, n):
      if self.sieve[i]:
        tmp = 2 * i
        while tmp < n:
          self.sieve[tmp] = False
          tmp += i
