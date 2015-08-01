# well, this is stupid easy

f = open('input/13.txt', 'r')

sum = 0
while True:
  line = f.readline()
  if not line:
    break
  sum += int(line)

print str(sum)[:10]
