from decor import clock
import functools


@functools.lru_cache()
@clock
def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

if __name__=='__main__':
    print(fibo(30))

