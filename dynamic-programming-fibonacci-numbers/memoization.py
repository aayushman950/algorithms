import sys
sys.setrecursionlimit(10000) 
cache = {0: 0, 1: 1}

def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

def reset_cache():
    global cache
    cache = {0: 0, 1: 1}