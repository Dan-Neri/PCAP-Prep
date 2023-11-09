from sys import path

path.append(f'{path[0]}\\modules')

for p in path:
    print(p)
    
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
