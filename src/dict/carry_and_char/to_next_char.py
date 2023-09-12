from data.chars import d
from data.chars import l

from hak.one.string.char.random_az import f as random_az
from hak.pf import f as pf
from hak.pxyf import f as pxyf

char_to_next_char = lambda char: l[((d[char] + 1) % len(l))]

# carry_and_char_to_next_char
# get_output_character
# carry, char
f = lambda x: char_to_next_char(x['char']) if x['carry'] else x['char']

def t_random_az():
  char = random_az()
  return pxyf({'carry': 0, 'char': char}, char, f)

def t():
  if not t_random_az(): return pf('!t_random_az')
  if not (lambda: pxyf({'carry': 1, 'char': '0'}, '1', f))(): return pf('!_0_1')
  if not (lambda: pxyf({'carry': 1, 'char': '1'}, '2', f))(): return pf('!_1_2')
  if not (lambda: pxyf({'carry': 1, 'char': '2'}, '3', f))(): return pf('!_2_3')
  if not (lambda: pxyf({'carry': 1, 'char': '3'}, '4', f))(): return pf('!_3_4')
  if not (lambda: pxyf({'carry': 1, 'char': '4'}, '5', f))(): return pf('!_4_5')
  if not (lambda: pxyf({'carry': 1, 'char': '5'}, '6', f))(): return pf('!_5_6')
  if not (lambda: pxyf({'carry': 1, 'char': '6'}, '7', f))(): return pf('!_6_7')
  if not (lambda: pxyf({'carry': 1, 'char': '7'}, '8', f))(): return pf('!_7_8')
  if not (lambda: pxyf({'carry': 1, 'char': '8'}, '9', f))(): return pf('!_8_9')
  if not (lambda: pxyf({'carry': 1, 'char': '9'}, ':', f))(): return pf('!_9_:')
  if not (lambda: pxyf({'carry': 1, 'char': 'a'}, 'b', f))(): return pf('!_a_b')
  if not (lambda: pxyf({'carry': 1, 'char': 'A'}, 'B', f))(): return pf('!_A_B')
  if not (lambda: pxyf({'carry': 1, 'char': 'b'}, 'c', f))(): return pf('!_b_c')
  if not (lambda: pxyf({'carry': 1, 'char': 'B'}, 'C', f))(): return pf('!_B_C')
  if not (lambda: pxyf({'carry': 1, 'char': 'c'}, 'd', f))(): return pf('!_c_d')
  if not (lambda: pxyf({'carry': 1, 'char': 'C'}, 'D', f))(): return pf('!_C_D')
  if not (lambda: pxyf({'carry': 1, 'char': 'd'}, 'e', f))(): return pf('!_d_e')
  if not (lambda: pxyf({'carry': 1, 'char': 'D'}, 'E', f))(): return pf('!_D_E')
  if not (lambda: pxyf({'carry': 1, 'char': 'e'}, 'f', f))(): return pf('!_e_f')
  if not (lambda: pxyf({'carry': 1, 'char': 'E'}, 'F', f))(): return pf('!_E_F')
  if not (lambda: pxyf({'carry': 1, 'char': 'f'}, 'g', f))(): return pf('!_f_g')
  if not (lambda: pxyf({'carry': 1, 'char': 'F'}, 'G', f))(): return pf('!_F_G')
  if not (lambda: pxyf({'carry': 1, 'char': 'g'}, 'h', f))(): return pf('!_g_h')
  if not (lambda: pxyf({'carry': 1, 'char': 'G'}, 'H', f))(): return pf('!_G_H')
  if not (lambda: pxyf({'carry': 1, 'char': 'h'}, 'i', f))(): return pf('!_h_i')
  if not (lambda: pxyf({'carry': 1, 'char': 'H'}, 'I', f))(): return pf('!_H_I')
  if not (lambda: pxyf({'carry': 1, 'char': 'i'}, 'j', f))(): return pf('!_i_j')
  if not (lambda: pxyf({'carry': 1, 'char': 'I'}, 'J', f))(): return pf('!_I_J')
  if not (lambda: pxyf({'carry': 1, 'char': 'j'}, 'k', f))(): return pf('!_j_k')
  if not (lambda: pxyf({'carry': 1, 'char': 'J'}, 'K', f))(): return pf('!_J_K')
  if not (lambda: pxyf({'carry': 1, 'char': 'k'}, 'l', f))(): return pf('!_k_l')
  if not (lambda: pxyf({'carry': 1, 'char': 'K'}, 'L', f))(): return pf('!_K_L')
  if not (lambda: pxyf({'carry': 1, 'char': 'l'}, 'm', f))(): return pf('!_l_m')
  if not (lambda: pxyf({'carry': 1, 'char': 'L'}, 'M', f))(): return pf('!_L_M')
  if not (lambda: pxyf({'carry': 1, 'char': 'm'}, 'n', f))(): return pf('!_m_n')
  if not (lambda: pxyf({'carry': 1, 'char': 'M'}, 'N', f))(): return pf('!_M_N')
  if not (lambda: pxyf({'carry': 1, 'char': 'n'}, 'o', f))(): return pf('!_n_o')
  if not (lambda: pxyf({'carry': 1, 'char': 'N'}, 'O', f))(): return pf('!_N_O')
  if not (lambda: pxyf({'carry': 1, 'char': 'o'}, 'p', f))(): return pf('!_o_p')
  if not (lambda: pxyf({'carry': 1, 'char': 'O'}, 'P', f))(): return pf('!_O_P')
  if not (lambda: pxyf({'carry': 1, 'char': 'p'}, 'q', f))(): return pf('!_p_q')
  if not (lambda: pxyf({'carry': 1, 'char': 'P'}, 'Q', f))(): return pf('!_P_Q')
  if not (lambda: pxyf({'carry': 1, 'char': 'q'}, 'r', f))(): return pf('!_q_r')
  if not (lambda: pxyf({'carry': 1, 'char': 'Q'}, 'R', f))(): return pf('!_Q_R')
  if not (lambda: pxyf({'carry': 1, 'char': 'r'}, 's', f))(): return pf('!_r_s')
  if not (lambda: pxyf({'carry': 1, 'char': 'R'}, 'S', f))(): return pf('!_R_S')
  if not (lambda: pxyf({'carry': 1, 'char': 's'}, 't', f))(): return pf('!_s_t')
  if not (lambda: pxyf({'carry': 1, 'char': 'S'}, 'T', f))(): return pf('!_S_T')
  if not (lambda: pxyf({'carry': 1, 'char': 't'}, 'u', f))(): return pf('!_t_u')
  if not (lambda: pxyf({'carry': 1, 'char': 'T'}, 'U', f))(): return pf('!_T_U')
  if not (lambda: pxyf({'carry': 1, 'char': 'u'}, 'v', f))(): return pf('!_u_v')
  if not (lambda: pxyf({'carry': 1, 'char': 'U'}, 'V', f))(): return pf('!_U_V')
  if not (lambda: pxyf({'carry': 1, 'char': 'v'}, 'w', f))(): return pf('!_v_w')
  if not (lambda: pxyf({'carry': 1, 'char': 'V'}, 'W', f))(): return pf('!_V_W')
  if not (lambda: pxyf({'carry': 1, 'char': 'w'}, 'x', f))(): return pf('!_w_x')
  if not (lambda: pxyf({'carry': 1, 'char': 'W'}, 'X', f))(): return pf('!_W_X')
  if not (lambda: pxyf({'carry': 1, 'char': 'x'}, 'y', f))(): return pf('!_x_y')
  if not (lambda: pxyf({'carry': 1, 'char': 'X'}, 'Y', f))(): return pf('!_X_Y')
  if not (lambda: pxyf({'carry': 1, 'char': 'y'}, 'z', f))(): return pf('!_y_z')
  if not (lambda: pxyf({'carry': 1, 'char': 'Y'}, 'Z', f))(): return pf('!_Y_Z')
  return 1
