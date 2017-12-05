# day 4 high-entropy passphrase

import sys

from sets import Set

lines = 0
valid = 0
try:
  with open("ip/d4.txt") as f:
    for line in f:
      lines = lines + 1
      a = Set()
      repeat = False
      for x in line.rstrip().split(" "):
        if x in a:
          repeat = True
          break
        else:
          a.add(x)

      if not repeat:
        if valid < 10:
          print a
        valid = valid + 1

except Exception as e:
  print type(e), e
  sys.exit(0)

print lines
print valid