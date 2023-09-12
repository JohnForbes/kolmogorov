from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.dict.carry_and_char.to_next_char import f as to_next_char
from src.dict.carry_and_char.to_next_carry import f as to_next_carry

def f(x):
  _x = list(x)
  chars = []
  carry = True
  while len(_x)>0:
    char = _x.pop()
    chars.append(to_next_char({'carry': carry, 'char': char}))
    carry = to_next_carry({'carry': carry, 'char': char})
  if carry: chars.append(' ')
  return ''.join(chars[::-1])

def t():
  if not (lambda: pxyf(  'a',    'b', f))(): return pf('!t_0')
  if not (lambda: pxyf(  '0',    '1', f))(): return pf('!t_1')
  if not (lambda: pxyf(  ' ',    '!', f))(): return pf('!t_2')
  if not (lambda: pxyf(  '~',   '  ', f))(): return pf('!t_3')
  if not (lambda: pxyf( '  ',   ' !', f))(): return pf('!t_4')
  if not (lambda: pxyf( '~~',  '   ', f))(): return pf('!t_5')
  if not (lambda: pxyf( 'aa',   'ab', f))(): return pf('!t_6')
  if not (lambda: pxyf('~~~', '    ', f))(): return pf('!t_7')
  return 1
