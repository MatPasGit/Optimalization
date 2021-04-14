import random

def init_problem_instance(p_size):
    starting_instance = list(range(p_size))

    #shuffle starting point
    random.shuffle(starting_instance)

    return starting_instance

def objective_function(instance,flow, distance ):
    objective = 0

    if isinstance(flow, list) and isinstance(instance,list) and isinstance(distance,list):

        for i in range(0 ,instance.size()):
            j = i+1
            if i == instance.size()-1:
                j=0

            objective += flow[instance[i]][instance[j]]*distance[i][j]

        return objective
    else:
        print("Bad entry data format")
        return -1
