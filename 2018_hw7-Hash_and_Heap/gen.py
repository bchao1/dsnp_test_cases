import numpy as np 
import numpy.random as random
from numpy.random import randint

task_nodes = []

def get_rand_key(max_len = 6):
    return ''.join([chr(ord('a') + randint(26)) for _ in range(max_len)])

def get_rand_value(low = 1, high = 100000):
    return randint(low, high + 1)

def get_taska_cmd():
    """ Assign load to minimum task node. """
    return 'taska -r {} {}\n'.format(str(randint(1, 101)), str(randint(1000, 10000)))

def get_taski_cmd():
    """ Initialize task manager. """
    return 'taski {}\n'.format(randint(10000, 20000))
    
def get_taskn_cmd():
    """ Insert new task nodes. """
    key, value = get_rand_key(), get_rand_value()
    task_nodes.append(key)
    return 'taskn -n {} {}\n'.format(key, value)

def get_taskq_cmd():
    """ Query task node. """
    args_list = ['str', 'ha', 'he', 'min']
    p = [0.25, 0.25, 0.25, 0.25]
    arg = random.choice(args_list, p = p)
    if arg == 'str':
        if task_nodes == []:
            return 'taskq {}\n'.format(get_rand_key())
        key = random.choice(task_nodes) if random.uniform() < 0.8 else get_rand_key()
        return 'taskq {}\n'.format(key)
    else:
        return 'taskq -{}\n'.format(arg)

def get_taskr_cmd():
    """ Remove task node. """
    if task_nodes == []:
        return 'taskr -n {}\n'.format(get_rand_key())
    key = random.choice(task_nodes) if random.uniform() < 0.8 else get_rand_key()
    return 'taskr -n {}\n'.format(key)

cmd_func = [get_taska_cmd, get_taskn_cmd, get_taskq_cmd, get_taskr_cmd]
cmd_prob = [0.2, 0.3, 0.3, 0.2]

dofile = ""
dofile += get_taski_cmd()

num_tests = 10000
for _ in range(num_tests):
    dofile += random.choice(cmd_func, p = cmd_prob)()
dofile += 'usage\nq -f\n'
with open('mydo', 'w') as file:
    file.write(dofile)
