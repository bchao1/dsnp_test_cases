import sys
import numpy as np
from numpy.random import uniform
from numpy.random import randint
from numpy.random import shuffle

if len(sys.argv) < 2:
    print("Illegal number of arguments!")
    exit()

test = int(sys.argv[1])
error_prob = 0  # Specify probability of illegal commands

cmd_list = ['mtn', 'mtd', 'mtp']  # `reset` command doesn't need to be extensively tested.
probs = [0.5, 0.3, 0.2]  # Specify probability of different commands.

def create_error(p = error_prob):
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
    if create_error(error_prob):  
        if uniform() > 0.5:
            opt += str(illegal_opt())  # Add an illegal option, ERROR!
        else:
            pass  # No option specified, ERROR!
    else:  # Add an integer option, (Can be 0 or negative -> ERROR!)
        opt += str(randint(-int(0.2 * max_n), max_n))
    return opt

def get_mtn_cmd():
    cmd = 'mtn'
    if create_error(error_prob * 0.1): # No options specified, ERROR!
        return cmd
    if create_error(error_prob * 0.1):
        return ' '.join([cmd, illegal_opt()])  # Specify an illegal option after 'mtn', ERROR!

    opts = [num_obj_opt(1, 10) if not create_error(error_prob) else '', \
            illegal_opt() if create_error(error_prob) else '', \
            special_opt('-a', 1024) if uniform() > 0.2 else '',]

    opts = list(filter(lambda opt: opt != '', opts))
    shuffle(opts)
    return cmd + ' ' + ' '.join(opts)

def get_mtd_cmd():
    cmd = 'mtd'
    if create_error(error_prob * 0.1): # No options specified, ERROR!
        return cmd
    if create_error(error_prob * 0.1):
        return ' '.join([cmd, illegal_opt()])  # Specify an illegal option after 'mtn', ERROR!
    
    opts = [(special_opt('-r', 10000) if uniform() > 0.3 else special_opt('-i', 1000)) \
            if not create_error(error_prob) else '',
            illegal_opt() if create_error(error_prob) else '', \
            '-a' if uniform() > 0.1 else '']

    opts = list(filter(lambda opt: opt != '', opts))
    shuffle(opts)
    return cmd + ' ' + ' '.join(opts)

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

dofile += 'mtr 0\nmtr 65536\nmtr 100\n'  # Test reset command. One check is sufficient.
dofile += 'usage -all\n'
dofile += "q -f\n"

with open("mydo", 'w') as file:
    file.write(dofile)