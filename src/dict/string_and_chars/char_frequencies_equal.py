from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.dict.string_and_char.count_char_freq import f as freq
from src.ints.all_equal import f as eq

f = lambda x: eq([freq({'string': x['string'], 'char': c}) for c in x['chars']])

t_0 = lambda: pxyf({'chars': ['l', 'a', 'r'], 'string': 'illawarra'}, 0, f)
t_1 = lambda: pxyf({'chars': ['l', 'r'], 'string': 'illawarra'}, 1, f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
