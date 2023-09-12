from hak.pxyf import f as pxyf
from hak.pf import f as pf

from src.dict.string_and_char_pairs.char_pair_frequencies_equal import f as cpfe
from src.dict.string_and_char.string_has_even_char_freq import f as e

# filter
f = lambda x: all([
  'x' in x,
  x[ 0] not in ' )}]',
  x[-1] not in ' ({[',
  e({'string': x, 'char': '"'}),
  e({'string': x, 'char': "'"}),
  cpfe({'string': x, 'char_pairs': [("(", ")"), ("{", "}"), ("[", "]")]})
])

def t():
  if not (lambda: pxyf('abc', 0, f))(): return pf('!t_0_no_x')
  if not (lambda: pxyf('axc', 1, f))(): return pf('!t_1_x')
  if not (lambda: pxyf(' x...', 0, f))(): return pf('!t_0_a')
  if not (lambda: pxyf(')x...', 0, f))(): return pf('!t_0_b')
  if not (lambda: pxyf('}x...', 0, f))(): return pf('!t_0_c')
  if not (lambda: pxyf(']x...', 0, f))(): return pf('!t_0_d')
  if not (lambda: pxyf('x... ', 0, f))(): return pf('!t_0_e')
  if not (lambda: pxyf('x...(', 0, f))(): return pf('!t_0_f')
  if not (lambda: pxyf('x...{', 0, f))(): return pf('!t_0_g')
  if not (lambda: pxyf('x...[', 0, f))(): return pf('!t_0_h')
  if not (lambda: pxyf("x'..'", 1, f))(): return pf('!t_1_i')
  if not (lambda: pxyf("x'.''", 0, f))(): return pf('!t_0_i')
  if not (lambda: pxyf('x".."', 1, f))(): return pf('!t_1_j')
  if not (lambda: pxyf('x".""', 0, f))(): return pf('!t_0_j')
  if not (lambda: pxyf('(){}[]]x', 0, f))(): return pf('!t_0_k')
  if not (lambda: pxyf('(){}[]x', 1, f))(): return pf('!t_1_k')
  return 1
