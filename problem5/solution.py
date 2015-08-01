from fractions import gcd

# least common multiple
def lcm(a, b):
  return a * b / gcd(a, b)

answer = 1

for i in range(1, 20):
  answer = lcm(answer, i)

print answer
