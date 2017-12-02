# day 2 corruption checksum

import sys

i = 0
try:
  with open("ip/d2p1.txt") as f:
    a = [[int(x) for x in line.split(" ")] for line in f]
except Exception as e:
  print type(e), e
  sys.exit(0)

def rowChecksum(row):
  n = len(row)
  for i in range(0, n):
    for j in range(0, n):
      if row[j] % row[i] == 0 and i != j:
        return row[j] / row[i]

sum = 0
for row in a:
  sum = sum + rowChecksum(row)

print sum