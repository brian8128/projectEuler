from array import array

k=13

numbers = array('h') # signed short
f = open('input/8.txt', 'r')

while True:
  c = f.read(1)
  if not c: 
    break
  if c.isdigit():
    numbers.append(int(c))

l = len(numbers)
max = 0

for i in range(0, l-k+1):
  product = 1;
  for j in range(i, i+k):
    product *= numbers[j]
  if product > max:
    max = product

print max
