from __future__ import print_function

class DNASequence(object):

    alphabet = 'ATGC'

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

    
    def gc_percent(self):
        return float(self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)



class AASequence(object):
   
    _water = 18.0153
    _weight_table = {'A': 89.0932, 'C': 121.1582, 'E': 147.1293,
                     'D': 133.1027, 'G': 75.0666, 'F': 165.1891,
                     'I': 131.1729, 'H': 155.1546, 'K': 146.1876,
                     'M': 149.2113, 'L': 131.1729, 'O': 255.3134,
                     'N': 132.1179, 'Q': 146.1445, 'P': 115.1305,
                     'S': 105.0926, 'R': 174.201, 'U': 168.0532,
                     'T': 119.1192, 'W': 204.2252, 'V': 117.1463,
                     'Y': 181.1885}

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
     return  sum([self._weight_table[aa] for aa in self.sequence]) - (len(self.sequence) - 1) * self._water
