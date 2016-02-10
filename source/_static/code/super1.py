from __future__ import print_function

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

    def to_fasta(self):
        id_ = self.name.replace(' ', '_') 
        fasta = '>{}\n'.format(id_)
        start = 0
        while start < len(self.sequence):
            end = start + 80
            fasta += self.sequence[start: end + 1] + '\n'
            start = end
        return fasta

    def molecular_weight(self):
        return sum([self._weight_table[x] for x in self.sequence]) - (len(self.sequence) - 1) * self._water


class RestrictionEnzyme(Sequence):

    def __init__(self, name, seq, cut, end):
        # the line below is in python3 only
        super().__init__(name, seq)
        # in python2 the syntax is
        # super(RestrictionEnzyme, self).__init__(name, seq)
        # this syntax is also available in python3
        self.cut = cut
        self.end = end


ecor1 = DNASequence('ecor I', 'GAATTC', 1, "sticky")
print(ecor1.name, len(ecor1))