# mask - * - любая послед-сть
#        ?/_ - любой 1 символ (даже 0)
from fnmatch import *
for x in range(0,10**9,23):
    if fnmatch(str(x),"12345?7?8"):
        print(x,x//23)