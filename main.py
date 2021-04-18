#Quadratic Assignment Problem QAP

#imports
from functions import *
from BB import *
from BS import *
from RandomNumberGenerator import *
import numpy as np

#global vars
problem_size=20


def generatorInstancji(Z,n):
    generator = RandomNumberGenerator(Z)
    d = []
    d = [[0 for i in range(n)] for j in range(n)]
    w = []
    w = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if (i > j):
                d[i][j] = generator.nextInt(1, 50)
                d[j][i] = d[i][j]
                w[i][j] = generator.nextInt(1, 50)
                w[j][i] = w[i][j]
    return w,d

if __name__ == '__main__':
    w,d = generatorInstancji(20, 5)
    print(np.matrix(w))
    print(np.matrix(d))

#implementację metody dokładnej(B & B) dla zadanego problemu(maksymalnie + 2.0 do oceny),
#implementację metody przybliżonej(BS) dla zadanego problemu(maksymalnie + 1.0 do oceny),
#jakość dolnych i górnych ograniczeń(maksymalnie + 1.0 do oceny),
#proste badania porównawcze(jakość/wydajność/zakres zastosowania) obu algorytmów(maksymalnie + 1.0 do oceny).
