from abc import ABCMeta, abstractmethod

# the syntax below is python3 specific
# for python 2 use the following syntax
#
# class Sequence(object)
#
#     __metaclass__ = ABCMeta
#

class Sequence(object, metaclass=ABCMeta):

    _water = 18.0153

    def __init__(self, name, seq):
        """
        :param seq: the sequence
        :type seq: string
        """
        self.name = name
        self.sequence = seq


    def __len__(self):
        """
        :return: the length of this sequence (number of bases or aa)
        :rtype: integer
        """
        return len(self.sequence)


    def to_fasta(self):
        """
        :return: a string in fasta format of this sequence
        :rtype: basestring
        """
        id_ = self.name.replace(' ', '_') 
        fasta = '>{}\n'.format(id_)
        start = 0
        while start < len(self.sequence):
            end = start + 80
            fasta += self.sequence[start: end + 1] + '\n'
            start = end
        return fasta


    def _one_strand_molec_weight(self, seq):
        """
        helper function to compute the mw of the seq
        :param seq: the seq (nucleic or proteic) to compute the mw
        :type seq: string
        :return: mw of seq
        :rtype: float
        """
        return sum([self._weight_table[base] for base in seq]) - (len(seq) - 1) * self._water


    @abstractmethod
    def molecular_weight(self):
        """
        tihis method is abstract and must be implemented in child classes
        :return: The molecular weight
        :rtype: float
        """
        pass

    @property
    def alphabet(self):
        return self._alphabet


class DNASequence(Sequence):

    _alphabet = 'ACGT'
    _weight_table = {'A': 347.2212, 'C': 323.1965, 'G': 363.2206, 'T': 322.2085}

    def gc_percent(self):
        """
        :return: the ratio of G and C bases in sequence
        :rtype: float
        """
        return float(self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)

    def molecular_weight(self):
        """
        :return: The molecular weight
        :rtype: float
        """
        direct_weight = super()._one_strand_molec_weight(self.sequence)
        rev_comp = self.rev_comp()
        rev_comp_weight = super()._one_strand_molec_weight(rev_comp.sequence)
        return direct_weight + rev_comp_weight

    def rev_comp(self):
        """
        :return: a new sequence representing the reverse complement
        :rtype: :class:`DNASequence` object
        """
        rev = self.sequence[::-1]
        table = str.maketrans(self._alphabet, self._alphabet[::-1])
        rev_comp = str.translate(rev, table)
        return DNASequence(self.name + '_reverse', rev_comp)


class AASequence(Sequence):

    _water = 18.0153
    _weight_table = {'A': 89.0932, 'C': 121.1582, 'E': 147.1293, 
                     'D': 133.1027, 'G': 75.0666, 'F': 165.1891, 
                     'I': 131.1729, 'H': 155.1546, 'K': 146.1876, 
                     'M': 149.2113, 'L': 131.1729, 'O': 255.3134, 
                     'N': 132.1179, 'Q': 146.1445, 'P': 115.1305, 
                     'S': 105.0926, 'R': 174.201, 'U': 168.0532, 
                     'T': 119.1192, 'W': 204.2252, 'V': 117.1463, 
                     'Y': 181.1885}

    _alphabet = ''.join(_weight_table.keys())

    def molecular_weight(self):
        """
        :return: The molecular weight
        :rtype: float
        """
        return super()._one_strand_molec_weight(self.sequence)

if __name__ == '__main__':

    nuc = DNASequence('Ecor I', 'GAATTC')
    prot = AASequence('my prot', 'MLEFVQ')

    for molec in [nuc, prot]:
        print(molec.name, molec.molecular_weight())
        print(molec.name, molec.alphabet)
        print('-' * 10)

    neither_nuc_nor_prot = Sequence('truc', 'GAATTC')