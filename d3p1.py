import math

def m_dist(a):
  n = int(math.ceil(math.sqrt(a)))

  if n % 2 == 0:
    n = n + 1

  m = (n + 1) / 2

  e = (2*n*n - 7*n + 7)/2
  no = (2*n*n - 5*n + 5)/2
  w = (2*n*n - 3*n + 3)/2
  s = (2*n*n - 1*n + 1)/2

  centers = [e, no, w, s]
  dist = map(lambda c: abs(a - c), centers)

  inwards = m - 1
  tang = min(dist)

  print ""
  print "a = ", a
  print "n = ", n
  print "centers = ", centers
  print  "dist = ", dist

  return inwards + tang

print m_dist(1)
print m_dist(12)
print m_dist(23)
print m_dist(1024)
print m_dist(16)

a = 325489

print m_dist(a)
