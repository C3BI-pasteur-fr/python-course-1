class Student:

    school = 'Pasteur'

    def __init__(self, name):
        self.name  = name
        self.scores = []

    def add_score(self, val):
        self.scores.append(val)

    def average(self):
        av = sum(self.scores)/len(self.scores)
        return av

st = Student('foo')
