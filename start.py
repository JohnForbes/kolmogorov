from src.filter import f as filter
from src.str.to_next_str import f as to_next_str
import os

with open('out.txt', 'rb') as _file:
  try:  # catch OSError in case of a one line file 
    _file.seek(-2, os.SEEK_END)
    while _file.read(1) != b'\n':
      _file.seek(-2, os.SEEK_CUR)
  except OSError:
    _file.seek(0)
  string = _file.readline().decode()

with open('out.txt', 'a') as _file:
  while 1:
    string = to_next_str(string)
    if filter(string):
      _file.write('\n'+string)
