import random

#tested
def init_problem_instance(p_size):
    starting_instance = list(range(p_size))

    #shuffle starting point
    random.shuffle(starting_instance)

    return starting_instance

#tested
def objective_function(instance, flow, distance ):
    objective = 0
    
    if isinstance(flow, list) and isinstance(instance,list) and isinstance(distance,list):

        for i in range(0 ,len(instance)):
            for j in range(i+1,len(instance)):
                objective += flow[instance[i]][instance[j]]*distance[i][j]

        return objective
    else:
        print("Bad entry data format")
        return -1
