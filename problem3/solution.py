

n = 600851475143

# Find the largest prime factor

i = 2

while i < n:
  while n % i == 0:
    n = n / i
    print n
  i += 1
print n
