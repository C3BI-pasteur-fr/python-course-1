from __future__ import print_function

class Sequence:

    __alphabet = 'ATGC'

    def __init__(self, name, seq):
        """
        :param seq: the sequence
        :type seq: string
        """
        self.name = name
        self.__sequence = seq

    def is_nucleic(self):
        is_nucleic = True
        for char in self.__sequence:
            if char not in self.__alphabet:
               is_nucleic = False
               break
        return is_nucleic


my_seq = Sequence('ecor1', 'GAATTC')

print(my_seq.is_nucleic())

print(my_seq.alphabet)

print(Sequence.alphabet)

print(my_seq._Sequence__alphabet)
