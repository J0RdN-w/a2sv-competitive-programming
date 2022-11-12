from math import ceil
(ln, width, siz) = (int(x) for x in input().split(' '))
print(ceil(ln/siz) * ceil(width/siz))
