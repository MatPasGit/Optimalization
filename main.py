#Quadratic Assignment Problem QAP

from functions import *
from BB import *
from BS import *
from RandomNumberGenerator import *
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import time

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

    wynikiBBtime=[]
    wynikiBStime=[]
    wynikiBBpoints=[]
    wynikiBSpoints=[]

    zakres=7
    for problem_size in range(3,3+zakres):

        #w - macierz przeplywów
        #d - macierz odległości
        w,d = generatorInstancji(20, problem_size)
        #print(np.matrix(w))

        lets_solve = BranchAndBound(w, d)
        start = time.time()
        lets_solve.solve()
        end = time.time()
        wynikiBBtime.append(end - start)
        wynikiBBpoints.append(lets_solve.upperBound)

        print("resolution:" , lets_solve.upperBound)
        print("instance: ", lets_solve.instance)
        print("how much similar results? : ", lets_solve.same_value_solution)

        lets_solveBS = BS(w, d)
        start = time.time()
        lets_solveBS.solve()
        end = time.time()
        wynikiBStime.append(end - start)
        wynikiBSpoints.append(lets_solveBS.upperBound)

        print("BS resolution:" , lets_solveBS.upperBound)
        print("BS instance: ", lets_solveBS.instance)
        print("BS how much similar results? : ", lets_solveBS.same_value_solution)

    argumenty = np.linspace(3,2+zakres,zakres)

    plt.plot(argumenty, wynikiBBtime, label="B&B")
    plt.plot(argumenty, wynikiBStime, label="BS")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla stałego ziarna")
    plt.legend()
    plt.savefig("WykresCzasuStaleZiarno.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSpoints, label="BS")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Wartość funkcji celu")
    plt.title("Wykres jakości rozwiązania problemu dla stałego ziarna")
    plt.legend()
    plt.savefig("WykresJakosciStaleZiarno.jpg", dpi=72)
    plt.show()

    wynikiBBtime.clear()
    wynikiBStime.clear()
    wynikiBBpoints.clear()
    wynikiBSpoints.clear()
    Z = RandomNumberGenerator(100)

    for problem_size in range(3, 3+zakres):

        #w - macierz przeplywów
        #d - macierz odległości
        w, d = generatorInstancji(Z.nextInt(10,100), problem_size)
        #print(np.matrix(w))

        lets_solve = BranchAndBound(w, d)
        start = time.time()
        lets_solve.solve()
        end = time.time()
        wynikiBBtime.append(end - start)
        wynikiBBpoints.append(lets_solve.upperBound)

        print("resolution:", lets_solve.upperBound)
        print("instance: ", lets_solve.instance)
        print("how much similar results? : ", lets_solve.same_value_solution)

        lets_solveBS = BS(w, d)
        start = time.time()
        lets_solveBS.solve()
        end = time.time()
        wynikiBStime.append(end - start)
        wynikiBSpoints.append(lets_solveBS.upperBound)

        print("BS resolution:", lets_solveBS.upperBound)
        print("BS instance: ", lets_solveBS.instance)
        print("BS how much similar results? : ",
              lets_solveBS.same_value_solution)

    plt.plot(argumenty, wynikiBBtime, label="B&B")
    plt.plot(argumenty, wynikiBStime, label="BS")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla zmiennego ziarna")
    plt.legend()
    plt.savefig("WykresCzasuZmienneZiarno.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSpoints, label="BS")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Wartość funkcji celu")
    plt.title("Wykres jakości rozwiązania problemu dla zmiennego ziarna")
    plt.legend()
    plt.savefig("WykresJakosciZmienneZiarno.jpg", dpi=72)
    plt.show()