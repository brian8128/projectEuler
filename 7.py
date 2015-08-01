from lib.sieve import Sieve

s = Sieve(1000000)

k=0
i=0

while k<10001:
  i+=1
  if s.isPrime(i):
    k+=1

print i
