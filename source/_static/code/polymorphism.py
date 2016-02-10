from __future__ import print_function

def my_sum(a, b):
    return a + b


print("my_sum(3, 4) =", my_sum(3, 4))
print("my_sum('three', 'four') =", my_sum('three', 'four'))


class Sequence(object):

    _water = 18.0153

    def __init__(self, name, seq):
        """
        :param seq: the sequence
        :type seq: string
        """
        self.name = name
        self.sequence = seq

    def __len__(self):
        return len(self.sequence)

    def __str__(self):
        return ">{}\n{}".format(self.name, self.sequence)

    def __add__(self, other):
        return Sequence('{}/{}'.format(self.name, other.name),
                        self.sequence + other.sequence)


ecor_1 = Sequence('Ecor_I', 'GAATTC')
bamh_1 = Sequence('Bamh I', 'GGATCC')

print("my_sum(ecor_1, bamh_1) =", my_sum(ecor_1, bamh_1))
