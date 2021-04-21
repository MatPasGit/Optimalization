# Quadratic Assignment Problem QAP


from functions import *
from BB import *
from BS import *
from RandomNumberGenerator import *
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import time
from tabulate import tabulate

def generatorInstancji(Z, n):
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
    return w, d


if __name__ == '__main__':

    wynikiBBtime = []
    wynikiBStime = []
    wynikiBSSecondtime = []
    wynikiBBpoints = []
    wynikiBSpoints = []
    wynikiBSSecondpoints = []

    zakres = 7
    table_niezmienne=[]
    table_niezmienne.append(["percentage of best kids ", "percentage away from proper value", "problem size(niezmienne ziarno)"])
    for problem_size in range(3, 3 + zakres):

        # w - macierz przeplywów
        # d - macierz odległości
        w, d = generatorInstancji(20, problem_size)
        # print(np.matrix(w))

        lets_solve = BranchAndBound(w, d)
        start = time.time()
        lets_solve.solve()
        end = time.time()
        wynikiBBtime.append(end - start)
        wynikiBBpoints.append(lets_solve.upperBound)

        print("resolution:", lets_solve.upperBound)
        print("instance: ", lets_solve.instance)
        print("how much similar results? : ", lets_solve.same_value_solution)

        for percent in range(20, 90, 10):
            lets_solveBS = BS(w, d, percent)
            start = time.time()
            lets_solveBS.solve()
            end = time.time()
            wynikiBStime.append(end - start)
            wynikiBSpoints.append(lets_solveBS.upperBound)

            print("BS resolution:", lets_solveBS.upperBound)
            print("BS instance: ", lets_solveBS.instance)
            print("BS how much similar results? : ", lets_solveBS.same_value_solution)

            lets_solveBSSecond = BS(w, d, percent)
            start = time.time()
            lets_solveBSSecond.solveSecond()
            end = time.time()
            wynikiBSSecondtime.append(end - start)
            wynikiBSSecondpoints.append(lets_solveBSSecond.upperBound)

            print("BS resolution:", lets_solveBSSecond.upperBound)
            print("BS instance: ", lets_solveBSSecond.instance)
            print("BS how much similar results? : ",
                  lets_solveBSSecond.same_value_solution)
            table_niezmienne.append([percent, ((lets_solveBSSecond.upperBound - lets_solve.upperBound)* 100)/lets_solve.upperBound , problem_size])


    argumenty = np.linspace(3, 2 + zakres, zakres)

    plt.plot(argumenty, wynikiBBtime, label="B&B")
    plt.plot(argumenty, wynikiBStime[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBStime[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBStime[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBStime[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBStime[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBStime[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBStime[6::7], label="BS - wnuki - 80")
    plt.plot(argumenty, wynikiBSSecondtime[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondtime[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondtime[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondtime[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondtime[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondtime[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondtime[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla stałego ziarna")
    plt.legend()
    plt.savefig("WykresCzasuStaleZiarno.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBStime[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBStime[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBStime[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBStime[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBStime[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBStime[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBStime[6::7], label="BS - wnuki - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla stałego ziarna - BS wnuki - różne procenty")
    plt.legend()
    plt.savefig("WykresCzasuStaleZiarnoBSWnuki.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBSSecondtime[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondtime[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondtime[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondtime[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondtime[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondtime[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondtime[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla stałego ziarna - BS dzieci - różne procenty")
    plt.legend()
    plt.savefig("WykresCzasuStaleZiarnoBSDzieci.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSpoints[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBSpoints[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBSpoints[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBSpoints[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBSpoints[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBSpoints[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBSpoints[6::7], label="BS - wnuki - 80")
    plt.plot(argumenty, wynikiBSSecondpoints[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondpoints[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondpoints[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondpoints[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondpoints[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondpoints[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondpoints[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Wartość funkcji celu")
    plt.title("Wykres jakości rozwiązania problemu dla stałego ziarna")
    plt.legend()
    plt.savefig("WykresJakosciStaleZiarno.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSpoints[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBSpoints[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBSpoints[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBSpoints[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBSpoints[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBSpoints[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBSpoints[6::7], label="BS - wnuki - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres jakości rozwiązania problemu dla stałego ziarna - BS wnuki - różne procenty")
    plt.legend()
    plt.savefig("WykresJakosciStaleZiarnoBSWnuki.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSSecondpoints[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondpoints[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondpoints[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondpoints[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondpoints[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondpoints[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondpoints[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres jakości rozwiązania problemu dla stałego ziarna - BS dzieci - różne procenty")
    plt.legend()
    plt.savefig("WykresJakosciStaleZiarnoBSDzieci.jpg", dpi=72)
    plt.show()

    wynikiBBtime.clear()
    wynikiBStime.clear()
    wynikiBSSecondtime.clear()
    wynikiBBpoints.clear()
    wynikiBSpoints.clear()
    wynikiBSSecondpoints.clear()
    Z = RandomNumberGenerator(100)

    table = []
    table.append(["percentage of best kids ","percentage away from proper value","problem size - zmienne ziarno" ])
    for problem_size in range(3, 3 + zakres):

        # w - macierz przeplywów
        # d - macierz odległości
        w, d = generatorInstancji(Z.nextInt(10, 100), problem_size)
        # print(np.matrix(w))

        lets_solve = BranchAndBound(w, d)
        start = time.time()
        lets_solve.solve()
        end = time.time()
        wynikiBBtime.append(end - start)
        wynikiBBpoints.append(lets_solve.upperBound)

        print("resolution:", lets_solve.upperBound)
        print("instance: ", lets_solve.instance)
        print("how much similar results? : ", lets_solve.same_value_solution)

        for percent in range(20, 90, 10):
            lets_solveBS = BS(w, d, percent)
            start = time.time()
            lets_solveBS.solve()
            end = time.time()
            wynikiBStime.append(end - start)
            wynikiBSpoints.append(lets_solveBS.upperBound)

            print("BS resolution:", lets_solveBS.upperBound)
            print("BS instance: ", lets_solveBS.instance)
            print("BS how much similar results? : ",
                  lets_solveBS.same_value_solution)

            lets_solveBSSecond = BS(w, d, percent)
            start = time.time()
            lets_solveBSSecond.solveSecond()
            end = time.time()
            wynikiBSSecondtime.append(end - start)
            wynikiBSSecondpoints.append(lets_solveBSSecond.upperBound)

            print("BS resolution:", lets_solveBSSecond.upperBound)
            print("BS instance: ", lets_solveBSSecond.instance)
            print("BS how much similar results? : ",
                  lets_solveBSSecond.same_value_solution)

            table.append([percent, ((lets_solveBSSecond.upperBound - lets_solve.upperBound)* 100)/lets_solve.upperBound , problem_size])

    plt.plot(argumenty, wynikiBBtime, label="B&B")
    plt.plot(argumenty, wynikiBStime[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBStime[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBStime[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBStime[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBStime[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBStime[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBStime[6::7], label="BS - wnuki - 80")
    plt.plot(argumenty, wynikiBSSecondtime[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondtime[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondtime[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondtime[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondtime[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondtime[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondtime[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla zmiennego ziarna")
    plt.legend()
    plt.savefig("WykresCzasuZmienneZiarno.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBStime[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBStime[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBStime[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBStime[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBStime[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBStime[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBStime[6::7], label="BS - wnuki - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla zmiennego ziarna - BS wnuki - różne procenty")
    plt.legend()
    plt.savefig("WykresCzasuZmienneZiarnoBSWnuki.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBSSecondtime[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondtime[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondtime[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondtime[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondtime[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondtime[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondtime[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title("Wykres czasu rozwiązania problemu dla zmienne ziarna - BS dzieci - różne procenty")
    plt.legend()
    plt.savefig("WykresCzasuZmienneZiarnoBSDzieci.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSpoints[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBSpoints[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBSpoints[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBSpoints[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBSpoints[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBSpoints[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBSpoints[6::7], label="BS - wnuki - 80")
    plt.plot(argumenty, wynikiBSSecondpoints[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondpoints[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondpoints[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondpoints[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondpoints[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondpoints[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondpoints[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Wartość funkcji celu")
    plt.title("Wykres jakości rozwiązania problemu dla zmiennego ziarna")
    plt.legend()
    plt.savefig("WykresJakosciZmienneZiarno.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSpoints[::7], label="BS - wnuki - 20")
    plt.plot(argumenty, wynikiBSpoints[1::7], label="BS - wnuki - 30")
    plt.plot(argumenty, wynikiBSpoints[2::7], label="BS - wnuki - 40")
    plt.plot(argumenty, wynikiBSpoints[3::7], label="BS - wnuki - 50")
    plt.plot(argumenty, wynikiBSpoints[4::7], label="BS - wnuki - 60")
    plt.plot(argumenty, wynikiBSpoints[5::7], label="BS - wnuki - 70")
    plt.plot(argumenty, wynikiBSpoints[6::7], label="BS - wnuki - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres jakości rozwiązania problemu dla zmiennego ziarna - BS wnuki - różne procenty")
    plt.legend()
    plt.savefig("WykresJakosciZmienneZiarnoBSWnuki.jpg", dpi=72)
    plt.show()

    plt.plot(argumenty, wynikiBBpoints, label="B&B")
    plt.plot(argumenty, wynikiBSSecondpoints[::7], label="BS - dzieci - 20")
    plt.plot(argumenty, wynikiBSSecondpoints[1::7], label="BS - dzieci - 30")
    plt.plot(argumenty, wynikiBSSecondpoints[2::7], label="BS - dzieci - 40")
    plt.plot(argumenty, wynikiBSSecondpoints[3::7], label="BS - dzieci - 50")
    plt.plot(argumenty, wynikiBSSecondpoints[4::7], label="BS - dzieci - 60")
    plt.plot(argumenty, wynikiBSSecondpoints[5::7], label="BS - dzieci - 70")
    plt.plot(argumenty, wynikiBSSecondpoints[6::7], label="BS - dzieci - 80")
    plt.grid(True)
    plt.xlabel("Rozmiar problemu (n)")
    plt.ylabel("Czas [s]")
    plt.title(
        "Wykres jakości rozwiązania problemu dla zmiennego ziarna - BS dzieci - różne procenty")
    plt.legend()
    plt.savefig("WykresJakosciZmienneZiarnoBSDzieci.jpg", dpi=72)
    plt.show()
    print(tabulate(table))
    print(tabulate(table_niezmienne))
