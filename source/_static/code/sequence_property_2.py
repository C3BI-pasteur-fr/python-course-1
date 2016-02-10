class Sequence:

    alphabet = 'ATGC'

    def __init__(self, name, seq):
        """
        :param seq: the sequence
        :type seq: string
        """
        self.name = name
        self.sequence = seq
        self.nucleic = True
        for char in self.sequence:
            if char not in self.alphabet:
                self.nucleic = False
                break


    def get_nucleic(self):
         return self._nucleic

    nucleic = property(get_nucleic)


ecor1 = Sequence('ecor I', 'GAATTC')
ecor1.nucleic = False
