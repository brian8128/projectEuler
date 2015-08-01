# There lots of good properties of pythagorean triples
# that could be exploited here but brute force will be O(n^2)
# which amounts to a million operations, which is easy

for a in range(1, 999):
  for b in range(a, 999):
    c = 1000 - a - b
    if (a * a + b * b == c * c):
      print a * b * c
