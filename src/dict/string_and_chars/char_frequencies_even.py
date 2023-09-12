from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.dict.string_and_char.string_has_even_char_freq import f as e

f = lambda x: all([e({'string': x['string'], 'char': c}) for c in x['chars']])

def t():
  if not (lambda: pxyf({'string': 'babcdc', 'chars': ['a', 'b']}, 0, f))():
    return pf('!t_a')
  
  if not (lambda: pxyf({'string': 'babcdc', 'chars': ['b', 'c']}, 1, f))():
    return pf('!t_b')

  if not (lambda: pxyf({'string': 'babcdc', 'chars': ['a', 'd']}, 0, f))():
    return pf('!t_d')
  
  return 1
