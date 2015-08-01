import numpy

n=20

grid = numpy.zeros((n+1, n+1))


for i in range(0, n+1):
  for j in range(0, n+1):
    if i==0 or j==0:
      grid[i][j] = 1
    else:
      grid[i][j] = grid[i-1][j] + grid[i][j-1]

print grid[-1][-1]


