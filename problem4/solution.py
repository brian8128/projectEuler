
def isPalendrome(n):
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False

biggest = 0;
for i in range(900, 999):
  for j in range(i, 999):
    if (i * j > biggest and isPalendrome(i*j)):
      biggest = i * j

print biggest
