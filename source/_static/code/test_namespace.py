from __future__ import print_function


class TestEnv:

    class_att = 1

    def __init__(self):
        self.inst_att = 2

    def test(self):
        loc_var = 3
        print("locals", locals())
        print("globals", globals())
        print("my self", self)
        print("my class", self.__class__)

t = TestEnv()

t.test()
