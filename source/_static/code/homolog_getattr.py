
Class Gene:

    def __init__(self, name, system, loner, profile):
        self.name = name
        self.profile = profile
        self._system = system
        self._loner = loner


    @property
    def system(self):
        """
        :return: the System that owns this Gene
        :rtype: :class:`macsypy.system.System` object
        """
        return self._system

    def __eq__(self, gene):
        """
        :return: True if the gene names (gene.name) are the same, False otherwise.
        :param gene: the query of the test
        :type gene: :class:`macsypy.gene.Gene` object.
        :rtype: boolean.
        """
        return self.name == gene.name


class Homolog:

    def __init__(self, gene, gene_ref, aligned=False):
        self.gene = gene
        self.ref = gene_ref
        self.aligned = aligned

    def __getattr__(self, name):
        return getattr(self.gene, name)

     def is_aligned(self):
        """
        :return: True if this gene homolog is aligned to its homolog, False otherwise.
        :rtype: boolean
        """
        return self.aligned