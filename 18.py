

f = open('input/18.txt', 'r')

lines = []

for line in f:
  lines.append(map(int, line.split(" ")))

# The problem is stated backwards to make it confusing.  
# Look at it forwards in order to solve.

lines.reverse()

maxPaths = []

# The maximum weight path that starts in the last row
# is just the weight of that position
maxPaths.append(lines[0])

for i in range(1, len(lines)):
  # calculate the next row of the max paths array
  # max path is the value of the node plus the larger
  # of the weights of the max path of the children
  row = []
  for j in range(0, len(lines[i])):
    row.append(lines[i][j] + max(maxPaths[i-1][j], maxPaths[i-1][j+1]))
  maxPaths.append(row)

print maxPaths
  
