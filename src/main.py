from hak.pf import f as pf

from src.dict.string_and_char_pairs.char_pair_frequencies_equal import f as cpfe
from src.dict.string_and_char.count_char_freq import f as freq
from src.str.to_next_str import f as to_next_str

def f(x):
  js_prefix = 'export const f=x=>'
  a = ' '
  functions = []
  while len(a)<(x-1):
    a = to_next_str(a)
    if all([
      'x' in a,
      a[0]!=' ',
      a[ 0]!=')', a[ 0]!='}', a[ 0]!=']',
      a[-1]!='(', a[-1]!='{', a[-1]!='[',
      not freq({'string': a, 'char': '"'}) % 2,
      not freq({'string': a, 'char': "'"}) % 2,
      cpfe({'string': a, 'char_pairs': [("(", ")"), ("{", "}"), ("[", "]")]})
    ]):
      # print(js_prefix+x)
      functions.append(a)
  return functions

def t():
  for (a, b) in [
    (1,     0),
    (2,     0),
    (3,     1),
    (4,   173),
    (5, 22462),
  ]:
    if len(f(a)) != b:
      return pf(f'len(f({a})) != {b}')
  return 1
