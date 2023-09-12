from hak.pxyf import f as pxyf
from hak.pf import f as pf

from data.chars import l
from data.chars import d

# get_output_carry
f = lambda x: (d[x['char']] + 1 >= len(l)) if x['carry'] else x['carry']

def t():
  if not (lambda: pxyf({'carry': 0, 'char': '%'}, 0, f))(): return pf('!t_a')
  if not (lambda: pxyf({'carry': 1, 'char': ' '}, 0, f))(): return pf('!t_b')
  if not (lambda: pxyf({'carry': 1, 'char': 'j'}, 0, f))(): return pf('!t_c')
  if not (lambda: pxyf({'carry': 1, 'char': '0'}, 0, f))(): return pf('!t_d')
  if not (lambda: pxyf({'carry': 1, 'char': '['}, 0, f))(): return pf('!t_e')
  if not (lambda: pxyf({'carry': 0, 'char': 'B'}, 0, f))(): return pf('!t_f')
  if not (lambda: pxyf({'carry': 0, 'char': 'F'}, 0, f))(): return pf('!t_g')
  if not (lambda: pxyf({'carry': 0, 'char': 'M'}, 0, f))(): return pf('!t_h')
  if not (lambda: pxyf({'carry': 0, 'char': '['}, 0, f))(): return pf('!t_i')
  if not (lambda: pxyf({'carry': 1, 'char': 'j'}, 0, f))(): return pf('!t_j')
  if not (lambda: pxyf({'carry': 1, 'char': '+'}, 0, f))(): return pf('!t_k')
  if not (lambda: pxyf({'carry': 1, 'char': 'y'}, 0, f))(): return pf('!t_l')
  if not (lambda: pxyf({'carry': 1, 'char': 'q'}, 0, f))(): return pf('!t_m')
  if not (lambda: pxyf({'carry': 1, 'char': ':'}, 0, f))(): return pf('!t_n')
  if not (lambda: pxyf({'carry': 0, 'char': 'q'}, 0, f))(): return pf('!t_o')
  if not (lambda: pxyf({'carry': 1, 'char': 'H'}, 0, f))(): return pf('!t_p')
  if not (lambda: pxyf({'carry': 1, 'char': ':'}, 0, f))(): return pf('!t_q')
  if not (lambda: pxyf({'carry': 1, 'char': "'"}, 0, f))(): return pf('!t_r')
  if not (lambda: pxyf({'carry': 1, 'char': 'a'}, 0, f))(): return pf('!t_s')
  if not (lambda: pxyf({'carry': 1, 'char': '0'}, 0, f))(): return pf('!t_t')
  if not (lambda: pxyf({'carry': 1, 'char': ' '}, 0, f))(): return pf('!t_u')
  if not (lambda: pxyf({'carry': 1, 'char': '~'}, 1, f))(): return pf('!t_v')
  if not (lambda: pxyf({'carry': 1, 'char': ' '}, 0, f))(): return pf('!t_w')
  if not (lambda: pxyf({'carry': 0, 'char': ' '}, 0, f))(): return pf('!t_x')
  if not (lambda: pxyf({'carry': 1, 'char': '~'}, 1, f))(): return pf('!t_y')
  if not (lambda: pxyf({'carry': 1, 'char': '~'}, 1, f))(): return pf('!t_z')
  return 1
