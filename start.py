from hak.one.directory.filepaths.get import f as get_filepaths
from hak.one.file.remove import f as remove_file
from hak.one.file.save import f as save_file
from hak.one.file.load import f as load_file
from time import sleep
from time import time

from src.str.is_well_formed import f as filter
from src.str.to_next_str import f as to_next_str

get_t = lambda: int(time()/900)*900

string = load_file('latest.txt')
latest = string
print(f'string: {repr(string)}')

while True:
  filepaths = get_filepaths('./signal', [])
  print(time(), filepaths)
  print(f'string: {repr(string)}')
  t = get_t()
  with open(f'./output/out_{t}.txt', 'a') as _file:
    for _ in range(600000):
      string = to_next_str(string)
      if filter(string):
        latest = string
        _file.write('\n'+latest)

  save_file('latest.txt', latest)
  
  if './signal/stop.signal' in filepaths:
    remove_file('./signal/stop.signal')
    break

print('fin')