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
        #starting solution
        #UB count
        #Queue
        for x in range(0, self.size ):
            self.resolutionsQueue.put(x)

        while( self.resolutionsQueue.empty() != True ):
            return 0
