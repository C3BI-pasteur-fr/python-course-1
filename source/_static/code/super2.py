

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


class DNASequence(Sequence):

    #sort of alpahbet is important to compute rev_comp
    _alphabet = 'AGCT'

    _weight_table = {'A': 331.2218, 'C': 307.1971, 'G': 347.2212, 'T': 322.2085}
    
    def gc_percent(self):
        return float(self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)

    def rev_comp(self):
        rev = self.sequence[::-1]
        table = str.maketrans(self._alphabet, self._alphabet[::-1])
        rev_comp = str.translate(rev, table)
        return DNASequence(self.name + '_reverse', rev_comp)

    def molecular_weight(self):
        #the following syntax can be used only in python3
        direct_weight = super().molecular_weight()
        rev_comp = self.rev_comp()
        rev_comp_weight = super(DNASequence, rev_comp).molecular_weight()
        return direct_weight + rev_comp_weight


class RNASequence(Sequence):

    _alphabet = 'AUGC'
    _weight_table = {'A': 347.2212, 'C': 323.1965, 'G': 363.2206, 'U': 324.1813}


class AASequence(Sequence):
   

    _weight_table = {'A': 89.0932, 'C': 121.1582, 'E': 147.1293, 
                     'D': 133.1027, 'G': 75.0666, 'F': 165.1891, 
                     'I': 131.1729, 'H': 155.1546, 'K': 146.1876, 
                     'M': 149.2113, 'L': 131.1729, 'O': 255.3134, 
                     'N': 132.1179, 'Q': 146.1445, 'P': 115.1305, 
                     'S': 105.0926, 'R': 174.201, 'U': 168.0532, 
                     'T': 119.1192, 'W': 204.2252, 'V': 117.1463, 
                     'Y': 181.1885}


ecor1 = DNASequence('ecor I', 'GAATTC')
print(ecor1.molecular_weight())