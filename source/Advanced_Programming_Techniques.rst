.. _Advanced Programming Techniques:

*******************************
Advanced Programming Techniques
*******************************


Generator
=========
https://docs.python.org/2/reference/expressions.html#generator-expressions
http://anandology.com/python-practice-book/iterators.html
>>> def fib():
...     a, b = 0, 1
...     while True:
...         yield a
...         a, b = b, a + b
... 

Recursivity
===========

def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


Closure
=======


Decorator
=========
https://wiki.python.org/moin/PythonDecoratorLibrary