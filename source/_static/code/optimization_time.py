import random
import sys


def algo_1(item, seq):
    return item in seq


def algo_2(item, seq):
    return item in seq

def compare_algo(item_number):
    l = range(item_number)
    l2 = l[:]
    random.shuffle(l)
    s = set(l)
    print "test algo1"
    for i in l2:
        algo_1(i, l)
        if not (i % 100):
            sys.stderr.write('.')
            sys.stderr.flush()
    print
            
    print"test algo2"
    for i in l2:
        algo_2(i, s)
        if not (i % 100):
            sys.stderr.write('.')
            sys.stderr.flush()
    print
        
compare_algo(100000)