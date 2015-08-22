import math

# Way better than this would be to do all the factorizations
# at the same time and then use the factorizations to find 
# the sum of the divisors quickly.  We could use the sieve
# to find these factorizations easily


def d(n):
  # sum of proper divisors of n
  # much faster would be to factor n but this should work
  sum = 0
  for i in range(1, int(n/2) + 1):
    if n % i == 0:
      sum += i
  return sum

dValues = [0] * 10001
for i in range(1, 10001):
  dValues[i] = d(i)

sum = 0

for i in range(1, 10001):
  if dValues[i] < 10001 and dValues[i] != i and dValues[dValues[i]] == i:
    sum += i

print sum
