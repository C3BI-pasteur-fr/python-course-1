def fib_gen():
    cache = {0 : 0,
             1 : 1}

    def fib(n):
        # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
        if n in cache:
            print "get {0} : {1} from cache".format(n, cache[n])
            return cache[n]
        else:
            print "call fib({0}) + fib({1})".format(n-1, n-2)
            res =  fib(n-1) + fib(n-2)
            cache[n] = res
            print "put {0} : {1} in cache".format(n, res)
            return res
    return fib


if __name__ == '__main__':
    import sys
    
    n = int(sys.argv[1])
    fib = fib_gen()
    resultat = fib(n)
    print resultat