from __future__ import print_function

class A(object):

    def met_1(self):
        print("A.meth_1")


class B(A):
    pass

class C(B):
    pass

class D(B):
    
    def met_1(self):
        print("D.meth_1")

class E(C, D):
    pass



e = E()

e.met_1()
