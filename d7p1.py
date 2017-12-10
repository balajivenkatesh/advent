# Day 7
# tags: regex, memoize, normalize, dfs

import sys
import re
from sets import Set

A = [] # list of id
h = {} # dependecies
p = {} # parent
W = {} # own wts
try:
  with open("ip/d7.txt") as f:
    for line in f:
      g = re.match(r"(\w+) \((\w+)\)(?: -> ((?:[a-z]+, )+\w+))?", line)

      a = g.group(1)
      A.append(a)

      wt = g.group(2)
      W[a] = int(wt)

      dep = g.group(3)
      dep = dep.split(", ") if dep is not None else []
      h[a] = dep
      for d in dep:
        p[d] = a
except Exception as e:
  print type(e), e
  sys.exit(0)

# #p1
bottom = ""
for a in A:
  if a not in p:
    bottom = a
    break

def get_odd_wt(all_d_wt):
  if all_d_wt[0] == all_d_wt[1]:
    p_d_wt = all_d_wt[0]
  elif all_d_wt[1] == all_d_wt[2]:
    return all_d_wt[0]
  else:
    return all_d_wt[1]
  for d_wt in all_d_wt:
    if d_wt != p_d_wt:
      return d_wt
  return -1

X = {} # total wt
def rec(curr):
  if len(h[curr]) == 0:
    wt = W[curr]
    X[curr] = wt
    return wt

  all_d_wt = []
  for d in h[curr]:
    all_d_wt.append(int(rec(d)))

  if len(all_d_wt) > 2:
    odd_wt = get_odd_wt(all_d_wt)
    if odd_wt != -1:
      print "o =", all_d_wt
      print "o =", odd_wt
      for d in h[curr]:
        print "y =", d, "w =", W[d]

  # print all_d_wt
  # print W[curr]
  X[curr] = sum(all_d_wt) + W[curr]

  # print X
  return X[curr]

rec(bottom)



