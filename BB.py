#imports
import queue
from functions import *

class BranchAndBound:

    instance = []
    flowList =[]
    distanceList=[]

    lowerBound = 0
    upperBound =0
    resolutionsQueue = queue.LifoQueue()

    #methods
    def BranchAndBound(self, initRandomInstance,w,d):
        self.instance = initRandomInstance
        self.flowList = w
        self.distanceList = d
        self.initLowerBound()


    def initLowerBound(self):
        self.lowerBound = objective_function(self.instance,self.flowList,self.distanceList)

    def initUpperBound(self):

    def countUpperBound(self):
        return 0