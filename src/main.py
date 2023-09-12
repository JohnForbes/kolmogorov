from hak.pf import f as pf

from src.str.to_next_str import f as to_next_str
from src.filter import f as filter

def f(x):
  string = ' '
  functions = []
  while len(string)<(x-1):
    string = to_next_str(string)
    if filter(string):
      functions.append(string)
  return functions

def t():
  for (a, b) in [
    (1,     0),
    (2,     0),
    (3,     1),
    (4,   172),
    (5, 22289),
  ]:
    if len(f(a)) != b:
      return pf(f'len(f({a})) != {b}')
  return 1
