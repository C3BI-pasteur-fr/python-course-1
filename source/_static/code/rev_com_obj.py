import string

class Sequence:

    # the order of the nucleotide in alphabet is important
    # to compute easily the revese complement
    alphabet = 'AGCT'

    def __init__(self, seq):
        """
        :param seq: the sequence
        :type seq: string
        """
        self.sequence = seq

    def reverse_comp(self):
        """
        :return: the reverse complement of this sequence
        :rtype: :class:`Sequence` instance
        """
        rev = self.sequence[::-1]
        table = string.maketrans(self.alphabet, self.alphabet[::-1])
        rev_comp = string.translate(self.sequence, table)
        return Sequence(rev_comp)


my_seq = Sequence('GAATTCC')
rev_comp = my_seq.reverse_comp()
print my_seq.sequence
print rev_comp.sequence
