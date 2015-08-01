# if n = p1^k^1 * p2^k2 * ... * ps^ks
# then n has (k1 + 1) * (k2 + 1) * (k3 + 1) * ... * (ks + 1) divisors
#
# triangular numbers are otf (n)(n+1)/2

n = 0
i = 1

while True:
  n+=i # n is now the ith triangular number
  i+=1
  tmp = n

  # count divisors using the formula above
  numDivisors = 1
  j = 2
  while tmp != 1:
    k = 0 # number of times j goes into n
    while tmp % j == 0:
      tmp = tmp / j
      k += 1
    numDivisors *= (k + 1)
    j+=1

  if numDivisors > 500:
    print n
    break
