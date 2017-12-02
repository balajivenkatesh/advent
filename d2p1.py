# day 2 corruption checksum

import sys

i = 0
try:
  with open("ip/d2p1.txt") as f:
    a = [[int(x) for x in line.split(" ")] for line in f]
except Exception as e:
  print type(e), e
  sys.exit(0)

sum = 0
for row in a:
  minX = min(row)
  maxX = max(row)
  sum = sum + maxX - minX

print sum