import sys

from functools import lru_cache
sys.setrecursionlimit(100000)
@lru_cache(None)
def f(n):
    if n<=1: return 0
    if n>1 and n%2==1: return f(n-1)+3*n**2
    if n>1 and n%2==0: return n/2+f(n-1)+2
print(f(1001))