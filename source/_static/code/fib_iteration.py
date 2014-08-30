def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    import sys
    
    n = int(sys.argv[1])
    resultat = fib(n)
    print resultat