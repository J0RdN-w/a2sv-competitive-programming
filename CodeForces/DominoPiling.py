from operator import mul

dims = (int(x) for x in input().split(' '))
print((mul(*dims))//2)