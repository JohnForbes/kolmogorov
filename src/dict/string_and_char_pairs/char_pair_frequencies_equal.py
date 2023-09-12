from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.dict.string_and_chars.char_frequencies_equal import f as char_freqs_eq
from src.ints.all_equal import f as all_equal

f = lambda x: all_equal([
  char_freqs_eq({'string': x['string'], 'chars': pair})
  for pair
  in x['char_pairs']
])

def t_0():
  x = {'string': '(){}[]]', 'char_pairs': [("(", ")"), ("{", "}"), ("[", "]")]}
  y = 0
  return pxyf(x, y, f)

def t_1():
  x = {'string': '()[]{}', 'char_pairs': [("(", ")"), ("{", "}"), ("[", "]")]}
  y = 1
  return pxyf(x, y, f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
