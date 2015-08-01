
n = 1000000

def next(n):
  if n%2 == 0:
    return n/2
  else:
    return 3*n+1

#lengths of chains
savedLengths = [0] * n

savedLengths[1] = 1

maxLength = 0
maxStart = 0

for i in range(2, n):
  current = i
  length = 0
  while current >= i:
    if current == i and length > 0:
      print "found a loop starting at " + str(i)
      break
    length += 1
    current = next(current)

  # current is now < i, so we know the length of the rest
  # of the chain
  length = length + savedLengths[current]
  # save the length of this chain
  savedLengths[i] = length

  if length > maxLength:
    maxLength = length
    maxStart = i

print maxStart
print maxLength


