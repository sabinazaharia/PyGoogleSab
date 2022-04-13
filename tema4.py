"""
Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
○ __init__ : instanțiem numărător și numitor
○ __str__ : afisam "numărător/numitor"
○ __add__ : returnam o noua fractie care reprezinta adunarea
○ __sub__: returnam o nouă fracție care reprezinta scădearea
○ inverse: returnează o nouă fracție (inversa fracției)
"""

class Fractie:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other):
        numarator = self.numarator * other.numitor + other.numarator * self.numitor
        numitor = self.numitor * other.numitor
        if numarator % numitor == 0:
            numarator /= numitor
            numitor /= numitor
        print(f'{numarator}/{numitor}')

    def __sub__(self, other):
        numarator = self.numarator * other.numitor - other.numarator * self.numitor
        numitor = self.numitor * other.numitor
        if numarator % numitor == 0:
            numarator /= numitor
            numitor /= numitor
        print(f'{numarator}/{numitor}')

    def inverse(self):
        aux = self.numarator
        self.numarator = self.numitor
        self.numitor = aux
        print(f'{self.numarator}/{self.numitor}')


f1 = Fractie(2, 6)
f2 = Fractie(4, 3)
print(f1)
print(f2)
f1.__add__(f2)
f1.__sub__(f2)
f1.inverse()
