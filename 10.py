from lib.sieve import Sieve

s = Sieve(2000000)

sum = 0

for i in range(1, 2000000):
  if s.isPrime(i):
    sum += i

print sum
