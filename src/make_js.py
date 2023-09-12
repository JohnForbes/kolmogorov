from hak.pf import f as pf

chars_list=[chr(_) for _ in range(32, 127)]
chars_dict={chr(_):_-32 for _ in range(32, 127)}

def __f(x):
  if len(x) == 1:
    _z, carry = _f(x)
    if not carry: return _z
    return ' '+_z
  if len(x) == 2:
    a, b = x[:-1], x[-1]
    _z, carry = _f(b)
    if not carry: return a+_z
    c, d = a[:-1], a[-1]
    return c+f(d)+_z
  raise NotImplementedError('!1')

def f(x):
  _x = list(x)
  _z = []
  carry = True
  while len(_x)>0:
    __x = _x.pop()
    if carry:
      q, carry = (_f(__x))
      _z.append(q)
    else:
      _z.append(__x)
  if carry:
    _z.append(' ')
  _z.reverse()
  return ''.join(_z)

def _f(previous):
  carry=False
  _index = chars_dict[previous]
  _next_index = _index + 1
  if _next_index >= len(chars_list):
    carry=True
    _next_index=0
  _next = chars_list[_next_index]
  return _next, carry

def t_0():
  x = 'a'
  y = 'b'
  z = f(x)
  return z==y or pf(['t_0, ',f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_1():
  x = '0'
  y = '1'
  z = f(x)
  return z==y or pf(['t_1', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_2():
  x = ' '
  y = '!'
  z = f(x)
  return z==y or pf(['t_2', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_3():
  x = '~'
  y = '  '
  z = f(x)
  return z==y or pf(['t_3', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_4():
  x = '  '
  y = ' !'
  z = f(x)
  return z==y or pf(['t_4', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_5():
  x = '~~'
  y = '   '
  z = f(x)
  return z==y or pf(['t_4', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_6():
  x = 'aa'
  y = 'ab'
  z = f(x)
  return z==y or pf(['t_4', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

def t_7():
  x = '~~~'
  y = '    '
  z = f(x)
  return z==y or pf(['t_4', f'x: {[x]}', f'y: {[y]}', f'z: {[z]}'])

t = lambda: all([
  t_0(),
  t_1(),
  t_2(),
  t_3(),
  t_4(),
  t_5(),
  t_6(),
  t_7()
])

if __name__ == '__main__':
  # print(t())
  prefix = 'export const f=x=>'
  x = ' '
  while len(x)<6:
    x = f(x)
    if all([
      'x' in x,
      x[0]!=' ',
      x[0]!=')',
      x[0]!='}',
      x[0]!=']',
      x[-1]!='(',
      x[-1]!='{',
      x[-1]!='[',
      not (len(x)-len(x.replace('"',''))) % 2,
      not (len(x)-len(x.replace("'",''))) % 2,
      (len(x)-len(x.replace("(",'')))==(len(x)-len(x.replace(")",''))),
      (len(x)-len(x.replace("{",'')))==(len(x)-len(x.replace("}",''))),
      (len(x)-len(x.replace("[",'')))==(len(x)-len(x.replace("]",'')))
    ]):
      print(prefix+x)
