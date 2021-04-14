#Quadratic Assignment Problem QAP
import random

problem_size=20;

def init_problem_instance(p_size):
    starting_instance = list(range(p_size))

    #shuffle starting point
    random.shuffle(starting_instance)

    return starting_instance

if __name__ == '__main__':
    print(init_problem_instance(problem_size))


