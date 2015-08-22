import csv

def intValue(c):
  return ord(c) - ord('A') + 1

def getSum(name):
  values = map(intValue, list(name))
  return sum(values)

reader = csv.reader(open('input/22.txt', 'r'))
names = reader.next()
names.sort()

sum_ = 0
for i in range(0, len(names)):
  sum_ += (i+1) * getSum(names[i])

print sum_
