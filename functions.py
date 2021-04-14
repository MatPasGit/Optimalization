def init_problem_instance(p_size):
    starting_instance = list(range(p_size))

    #shuffle starting point
    random.shuffle(starting_instance)

    return starting_instance