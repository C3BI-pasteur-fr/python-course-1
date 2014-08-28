def memoize(func):
    cache = {}
    def inner_func(arg):
        if n in cache:
            return cache(n)
        else:
            res = func(*args, **kwargs)
            cache[arg] = res
            return res
    return inner_func

@memoize
def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
    
factorial = memoize(factorial) 
    
    
if __name__ == '__main__':
    import sys
    
    n = int(sys.argv[1])
    resultat = fib(n)
    print resultat