class Sieve:
    'For telling which numbers are prime and which are composite.'
    'Construction is O(nlog(log(n))), lookups constant time thereafter.'
    'Memory used is O(n)'

    def __init__(self, n):
        # array of n booleans initalized to true
        self.sieve = [True] * (n/2)
        # 1 is not prime
        self.sieve[1/2] = False
        for i in range(3, n, 2):
            # If i is prime, mark all the multiples of i as composite
            if self.sieve[i/2]:
                # 2 * i is even so we already know that's composite
                tmp = 3 * i
                while tmp < n:
                    self.sieve[tmp/2] = False
                    # tmp + i is even, advance to next odd multiple of i
                    tmp += 2 * i

    def isPrime(self, k):
        if k % 2 == 0:
            if k == 2:
                return True
            else:
                return False
        else:
            return self.sieve[k/2]
