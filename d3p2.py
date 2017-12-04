import math

def print_p(p):
  print "len(p) =", len(p)
  if len(p) >= 6:
    return

  for row in p:
    print row

def get_p_xy(p, x, y):
  return p[x - 1][y - 1] + p[x - 1][y] + p[x - 1][y  + 1] + p[x][y - 1] + p[x][y + 1] + p[x + 1][y - 1] + p[x + 1][y] + p[x + 1][y + 1]

def first_val(a):
  n = int(math.ceil(math.sqrt(a)))

  if n % 2 == 0:
    n = n + 1

  m = (n + 1) / 2

  nn = n
  p = [[0 for x in range(nn)] for y in range(nn)]

  x = m - 1
  y = m - 1
  i = 1

  p[x][y] = 1

  y = y + 1
  side = 3

  go = "N"
  while True:
    i = i + 1
    op = get_p_xy(p, x, y)
    p[x][y] = op
    if go == "N":
      if i == side*(side - 3) + 3:
        go = "W"
      else:
        x = x - 1
    if go == "W":
      if i == side*(side - 2) + 2:
        go = "S"
      else:
        y = y - 1
    if go == "S":
      if i == side*(side - 1) + 1:
        go = "E"
      else:
        x = x + 1
    if go == "E":
      y = y + 1
      if i == side*(side):
        go = "N"
        side = side + 2

    if op > a:
      # print_p(p)
      return op

print first_val(325489)