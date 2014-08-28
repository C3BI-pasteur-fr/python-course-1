
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
if __name__ == '__main__':
    import sys
    
    n = int(sys.argv[1])
    fib = fib_generator()
    for i, resultat in enumerate(fib):
        if i >= n:
            break
    print resultat