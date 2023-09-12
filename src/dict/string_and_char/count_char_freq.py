from hak.pxyf import f as pxyf

# count
# string, char
f = lambda x: len(x['string'])-len(x['string'].replace(x['char'],''))

t = lambda: pxyf({'string': 'illawarra', 'char': 'a'}, 3, f)
