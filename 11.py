import numpy

n=20
k=4

grid = numpy.zeros(shape=(n,n))
f = open('input/11.txt', 'r')

for i in range(0, n):
  line = f.readline()
  row = map(int, line.split(" "))
  for j in range(0, n):
    grid[i][j] = row[j]

# ok we've loaded the grid into a numpy matrix

# for each point in the array check if it is the leftmost, topmost, or upper corner
# of a good diagonal
biggest = 0

x=0
y=0

for i in range(0, n):
  for j in range(0, n):

    if i <= n-4 :
      # Check if (i,j) is the topmost of a good product
      product = 1
      for s in range(0, 4):
        product *= grid[i+s][j]
      if product > biggest:
        biggest = product;

    if j <= n-4 :
      # Check if (i,j) is the leftmost of a good product
      product = 1
      for s in range(0, 4):
        product *= grid[i][j+s]
      if product > biggest:
        biggest = product;

    if i <= n-4 and j <= n-4:
      # Check if (i,j) is the leftmost of a good product
      product = 1
      for s in range(0, 4):
        product *= grid[i+s][j+s]
      if product > biggest:
        biggest = product;

    if i >= 4 and j <= n-4:
      # Check if (i,j) is the leftmost of a good product
      product = 1
      for s in range(0, 4):
        product *= grid[i-s][j+s]
      if product > biggest:
        biggest = product;


print biggest
print x
print y
