from src.str.js.get_next import f as make_js
from hak.pf import f as pf

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
  if len(f(1)) !=     0: return pf('len(f(1)) !=     0')
  if len(f(2)) !=     0: return pf('len(f(2)) !=     0')
  if len(f(3)) !=     1: return pf('len(f(3)) !=     1')
  if len(f(4)) !=   173: return pf('len(f(4)) !=   173')
  if len(f(5)) != 22462: return pf('len(f(5)) != 22462')
  return 1
