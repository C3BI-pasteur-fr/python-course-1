def fib_gen():
    cache = {0 : 0,
             1 : 1}

    def fib(n):
        # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
        if n in cache:
            return cache[n]
        else:
            res =  fib(n-1) + fib(n-2)
            cache[n] = res
            return res
    return fib


if __name__ == '__main__':
    import sys
    
    n = int(sys.argv[1])
    fib = fib_gen()
    resultat = fib(n)
    print resultat