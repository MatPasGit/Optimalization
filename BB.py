#imports
import queue
from functions import *

class BranchAndBound:

    instance = []
    flowList =[]
    distanceList=[]
    size = 0

    lowerBound = 0
    upperBound =0
    resolutionsQueue = queue.LifoQueue()

    #methods

    def BranchAndBound(self, initRandomInstance,w,d, problem_size):
        self.instance = initRandomInstance
        self.flowList = w
        self.distanceList = d
        self.size = problem_size
        self.initLowerBound()



    def initLowerBound(self):
        self.lowerBound = objective_function(self.instance,self.flowList,self.distanceList)

    def countLowerBound(self,instance):
        lb = objective_function(instance, self.flowList, self.distanceList)
        return lb


    def initUpperBound(self):

    def countUpperBound(self):
        return 0

    def solve(self):
        resolution = []
        #starting solution
        #UB count
        UB=0 #DO POPRAWY JAK PIERON
        #Queue
        for x in range(0, self.size ):
            temp_instance=[[x],UB] #TU POWINNO SIE LICZYC PIERWSZA WARTOSC ZAMIAST UB
            self.resolutionsQueue.put(temp_instance)

        while( self.resolutionsQueue.empty() != True ):

            instance = self.resolutionsQueue.get()

            # if is leave
            if(len(instance) == self.size):
                inst_value = objective_function(instance,self.flowList, self.distanceList)
                if( inst_value < UB ):
                    resolution  = instance
                    UB  = inst_value
            else:
                for x in range(0,self.size):
                    #uzupełnij dzieci poprzedniego ale dupiato narazie to jest


            return 0
