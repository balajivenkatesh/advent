# day 4 high-entropy passphrase

import sys

from sets import Set

valid = 0
try:
  with open("ip/d4.txt") as f:
    for line in f:
      a = Set()
      repeat = False
      for y in line.rstrip().split(" "):
        x = ''.join(sorted(y))
        if x in a:
          repeat = True
          break
        else:
          a.add(x)

      if not repeat:
        valid = valid + 1

except Exception as e:
  print type(e), e
  sys.exit(0)

print valid