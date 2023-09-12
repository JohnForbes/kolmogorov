from hak.pxyf import f as pxyf
from hak.pf import f as pf

from src.dict.string_and_char.count_char_freq import f as freq

f = lambda x: not freq(x) % 2

def t():
  if not (lambda: pxyf({'string': 'bab', 'char': 'a'}, 0, f))():
    return pf('!t_a')
  
  if not (lambda: pxyf({'string': 'bab', 'char': 'b'}, 1, f))():
    return pf('!t_b')
  
  return 1
