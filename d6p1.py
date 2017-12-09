import math
from sets import Set

a = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
n = 16
h = {}
count = 0

last = 99999999999
while True:
  str = "".join(map(lambda c: chr(c + 65), a))
  print str
  if str in h:
    last = h[str]
    break
  else:
    h[str] = count
    count += 1

  m = max(a)
  x = a.index(m)

  diff = int(math.ceil(m / float(n)))

  if m > 16:
    print "GGGGGGGG"

  for i in range(1, m + 1):
    a[(x + i) % n] += 1
  a[x] = 0

print count - last