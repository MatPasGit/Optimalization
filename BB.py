#imports
import copy
import queue
from functions import *
from Node import *

class BranchAndBound:

    instance = []
    flowList =[]
    distanceList=[]
    size = 0
    same_value_solution = 0

    upperBound =0
    resolutionsQueue = queue.LifoQueue()

    #methods

    def  __init__(self, w,d):
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

        #inicjowanie potencjalnie najlepszego rozwiazania (najlepsze rozwiązanie z kilku losowych)
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
                for x in range(0,self.size):
                    if x in instance.node_list: #jesli zaklad zostal juz przydzielony pomiń
                        continue

                    child_list = copy.copy(instance.node_list)
                    child_list.append(x)
                    child = Node(child_list, objective_function(child_list,self.flowList, self.distanceList))

                    if child.value > self.upperBound: ##jeśli wartość tymczasowego rozwiazanie jest wieksza od upperBound nie rozwijaj drzewa dalej
                        continue

                    self.resolutionsQueue.put(child)


