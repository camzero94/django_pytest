

def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


cache = {}


def fib_cached(n: int):

    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n

    fn = fib_cached(n-2) + fib_cached(n-1)
    cache[n] = fn
    return fn
