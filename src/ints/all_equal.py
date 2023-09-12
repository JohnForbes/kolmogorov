from hak.one.number.int.random.make import f as make_int
from hak.pxyf import f as pxyf
from hak.pf import f as pf

f = lambda x: all([x[0] == x_i for x_i in x])

t_0 = lambda: pxyf([-3, -2, -1, 0, 1, 2, 3], 0, f)

def t_1():
  i = make_int(-9, 9)
  return pxyf([i for _ in range(10)], 1, f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
