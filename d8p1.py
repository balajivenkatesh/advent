# Day 8
# tags: regex

import sys
import re

def do_op(cond_reg_val, cond_val, cond):
  if cond == "<=":
    return cond_reg_val <= cond_val
  elif cond == "<":
    return cond_reg_val < cond_val
  elif cond == ">=":
    return cond_reg_val >= cond_val
  elif cond == ">":
    return cond_reg_val > cond_val
  elif cond == "!=":
    return cond_reg_val != cond_val
  elif cond == "==":
    return cond_reg_val == cond_val
  else:
    raise "Invalid op"

max_reg_val = 0
all_max_reg_val = 0
max_reg = ""
all_reg = {}

try:
  with open("ip/d8.txt") as f:
    for line in f:
      g = re.match(r"([a-z]+) (inc|dec) (-?[0-9]+) if ([a-z]+) (<=|<|>=|>|==|!=) (-?[0-9]+)", line)

      reg = g.group(1)

      if reg in all_reg:
        reg_val = all_reg[reg]
      else:
        reg_val = 0
        all_reg[reg] = reg_val

      op = g.group(2)
      diff = int(g.group(3))

      if op == "dec":
        reg_val -= diff
      else: # "inc"
        reg_val += diff

      cond_reg = g.group(4)
      if cond_reg in all_reg:
        cond_reg_val = all_reg[cond_reg]
      else:
        cond_reg_val = 0
        all_reg[cond_reg] = cond_reg_val

      cond = g.group(5)
      cond_val = int(g.group(6))

      if do_op(cond_reg_val, cond_val, cond):
        all_reg[reg] = reg_val
        if reg_val > all_max_reg_val:
          all_max_reg_val = reg_val

except Exception as e:
  print type(e), e
  sys.exit(0)


for reg in all_reg:
  reg_val = all_reg[reg]
  if reg_val > max_reg_val:
    max_reg_val = reg_val
    max_reg = reg

print "max =", max_reg_val
print "all_max =", all_max_reg_val