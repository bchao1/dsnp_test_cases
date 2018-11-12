import sys
import numpy as np
from numpy.random import uniform
from numpy.random import randint
from numpy.random import shuffle



cmd_list = ['mtn', 'mtd', 'mtp', 'mtr']
probs = ['0.45', '0.45', '0.05', '0.05']

def create_error(p = 0.1):
    """ Specify the probability to create an invalid option """
    return uniform() < p

def illegal_opt():
    """ Return a random sequence of characters """
    return ''.join([chr(randint(65, 126)) for _ in range(int(5 * uniform()))])

def num_obj_opt(low, high):
    """ Return an integer in range [low, high) indicating number of objects 
    to allocate """
    return str(randint(low, high))

def special_opt(opt_type, max_n):
    """ Returns three kinds of options, specified by 'opt_type'.
    Args:
        type: Option type from ['-r', '-i', '-a'] 
        n: random integer range
    Returns:
        opt: a valid or invalid option.
    """

    opt = opt_type + ' '  # Base command
    if create_error():  
        if uniform() > 0.5:
            opt += str(illegal_opt())  # Add an illegal option, ERROR!
        else:
            pass  # No option specified, ERROR!
    else:  # Add an integer option, (Can be 0 or negative -> ERROR!)
        opt += str(randint(-int(0.2 * max_n), max_n))
    return opt

def get_mtn_cmd():
    cmd = 'mtn'
    if create_error(0.05): # No options specified, ERROR!
        return cmd
    if create_error():
        return ' '.join([cmd, illegal_opt()])  # Specify an illegal option after 'mtn', ERROR!

    opts = [num_obj_opt(-100, 1000) if not create_error(0.2) else '', \
            illegal_opt() if create_error(0.2) else '', \
            special_opt('-a', 100) if uniform() > 0.5 else '',]

    opts = list(filter(lambda opt: opt != '', opts))
    shuffle(opts)
    return cmd + ' ' + ' '.join(opts)

def get_mtd_cmd():
    cmd = 'mtd'
    if create_error(0.05): # No options specified, ERROR!
        return cmd
    if create_error():
        return ' '.join([cmd, illegal_opt()])  # Specify an illegal option after 'mtn', ERROR!
    
    opts = [(special_opt('-r', 10000) if uniform() > 0.5 else special_opt('-i', 10000)) \
            if not create_error(0.2) else '',
            illegal_opt() if create_error(0.2) else '', \
            '-a' if uniform() > 0.5 else '']

    opts = list(filter(lambda opt: opt != '', opts))
    shuffle(opts)
    return cmd + ' ' + ' '.join(opts)


test = 1000
if len(sys.argv) > 1:
    test = int(sys.argv[1])

dofile = ""
for _ in range(test):

    cmd = np.random.choice(cmd_list)
    if cmd == 'mtn':
        line = get_mtn_cmd()
    elif cmd == 'mtd':
        line = get_mtd_cmd()
    else:
        line = cmd

    line += '\n'
    dofile += line
dofile += "q -f\n"

with open("mydo", 'w') as file:
    file.write(dofile)