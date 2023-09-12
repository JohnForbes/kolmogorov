from hak.pf import f as pf

from src.str.to_next_str import f as make_js

def f(x):
  js_prefix = 'export const f=x=>'
  a = ' '
  functions = []
  while len(a)<(x-1):
    a = make_js(a)
    if all([
      'x' in a,
      a[0]!=' ',
      a[ 0]!=')', a[ 0]!='}', a[ 0]!=']',
      a[-1]!='(', a[-1]!='{', a[-1]!='[',
      not (len(a)-len(a.replace('"',''))) % 2,
      not (len(a)-len(a.replace("'",''))) % 2,
      (len(a)-len(a.replace("(",'')))==(len(a)-len(a.replace(")",''))),
      (len(a)-len(a.replace("{",'')))==(len(a)-len(a.replace("}",''))),
      (len(a)-len(a.replace("[",'')))==(len(a)-len(a.replace("]",'')))
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
