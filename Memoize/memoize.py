def memoize(fn):
    cache = {}
    call_count = 0

    def memoized_fn(*args):
        nonlocal call_count
        key = tuple(args)

        if key in cache:
            return cache[key]
        else:
            call_count += 1
            result = fn(*args)
            cache[key] = result
            return result

    memoized_fn.getCallCount = lambda: call_count
    
    return memoized_fn

def sum_fn(a, b):
    return a + b

def fib_fn(n):
    if n <= 1:
        return 1
    return fib_fn(n - 1) + fib_fn(n - 2)

def factorial_fn(n):
    if n <= 1:
        return 1
    return n * factorial_fn(n - 1)