#imports
import copy
import operator
import queue

from numpy import sort

from functions import *
from Node import *

class BS:

    instance = []
    flowList =[]
    distanceList=[]
    size = 0
    same_value_solution = 0

    upperBound =0
    resolutionsQueue = queue.Queue()

    percentage_acceptable = 60

    #methods

    def  __init__(self,w,d):
        self.flowList = w
        self.distanceList = d
        self.size = len(w)

    def initUpperBound(self):
        best = 0
        for x in range(0, 9):
            problem_list = init_problem_instance(self.size)

            if x == 0:
                best = objective_function(problem_list, self.flowList, self.distanceList)
                continue

            problem_value = objective_function(problem_list, self.flowList, self.distanceList)
            if problem_value >= best:
                best = problem_value

        self.upperBound = best



    def solve(self):

        #inicjowanie potencjalnie najlepszego rozwiazania
        self.initUpperBound()

        for x in range(0, self.size ): #dodaj pierwsze node'y
            temp_instance=Node([x], objective_function([x],self.flowList, self.distanceList))
            self.resolutionsQueue.put(temp_instance)

        while( self.resolutionsQueue.empty() != True ):

            instance = self.resolutionsQueue.get()

            if(len(instance.node_list) == self.size): #jesli jest lisciem
                if instance.value < self.upperBound : # jezeli rozwiazanie lepsze to je zapisz
                    self.instance = copy.copy(instance.node_list)
                    self.upperBound = copy.copy(instance.value)
                    self.same_value_solution = 0
                    print("New value: ", self.upperBound, "New best sequence", self.instance)
                if instance.value == self.upperBound:
                    self.same_value_solution += 1

            else: ##jeśli nie jest liściem
                best_kids_of_all_time = []
                bs_child_list  = []
                for x in range(0,self.size): #kolejne dzieci
                    if x in instance.node_list: #jesli zaklad zostal juz przydzielony pomiń
                        continue

                    child_list = copy.copy(instance.node_list)
                    child_list.append(x)
                    bs_child_list.append(Node(child_list, objective_function(child_list,self.flowList, self.distanceList)))
                    ##dodanie wszystkich dzieci do listy


                for bs in bs_child_list:## zachłannie przydzielana wartosc dla dziecka dziecka
                    best_child = []
                    best = 0

                    for x in range( 0, self.size): #ZNAJDZ NAJLEPSZE DZIECKO I ZAPISZ DO BEST I BEST_CHILD
                        if x in bs.node_list:
                            continue

                        child = copy.copy(bs.node_list)
                        child.append(x)
                        if best_child == [] : # jesli pusty to ustaw pierwszy
                            best_child = copy.copy(child)
                            best = objective_function(best_child, self.flowList, self.distanceList)
                        
                        c = objective_function(child, self.flowList, self.distanceList)

                        if  c < best:
                            best_child = copy.copy(child)
                            best = c #Najlepsze dziecko dziecka (najlepszy wnuk)

                    best_kids_of_all_time.append(Node(best_child, best))

                newlist = sorted(best_kids_of_all_time, key=operator.attrgetter("value"))
                elements_count = int((len(newlist) * (self.percentage_acceptable/100) )) + 1

                for x in range(0,elements_count):
                    elem = copy.copy(newlist[x])
                    if elem.value > self.upperBound: ##jeśli wartość tymczasowego rozwiazanie jest wieksza od upperBound nie rozwijaj drzewa dalej
                        continue
                self.resolutionsQueue.put(elem)

        return 0
