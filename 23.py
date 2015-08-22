

def getCount(k):
  'returns the number of divisors of n, given the list of powers'
  'of its prime factors'
  n = 1
  for i in range(0, len(k)):
    n = n * (k[i] + 1)
  return n

def enumerate(k):
  'Given an array [k1, k2, ... , kr] of positive integers we'
  'want a list of all arrays [s1, ... , sr,] of integers such'
  'that 0 <= s_i <= k_i'

  n = getCount(k)
  result = []
  for i in range(0, n):
    tmp = i
    current = [0] * len(k)
    for j in range(0, len(k)):
      current[j] = tmp % (k[j] + 1)
      tmp /= (k[j] + 1)
    result.append(current)
  return result

def getDivisors(primeFactors, powers):
  'Gets all the divisors of an integer, given its factorization'
  n = getCount(powers)
  result = []
  # list of all the possible exponent arrays that a divisor 
  # could have
  eaList = enumerate(powers)
  for ea in eaList:
    divisor = 1
    for i in range(0, len(primeFactors)):
      divisor *= primeFactors[i] ** ea[i]
    result.append(divisor)
  return result

primeFactors = [2, 3]
powers = [1, 2]

print getDivisors(primeFactors, powers)
