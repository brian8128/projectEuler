
prev = 0
curr = 1
sum = 0

while curr < 4000000:
  if curr % 2 == 0:
    sum += curr
  tmp = curr + prev
  prev = curr
  curr = tmp

print sum

