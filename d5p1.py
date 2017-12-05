# day 5 jumps

import sys

try:
  with open("ip/d5.txt") as f:
    a = [int(line) for line in f]
except Exception as e:
  print type(e), e
  sys.exit(0)

n = len(a)
i = 0
c = 0

while i < n:
  jump = a[i]
  a[i] = jump + 1
  i = i + jump
  c = c + 1

print c