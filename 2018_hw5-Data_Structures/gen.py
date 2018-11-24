import sys
import numpy as np
from numpy.random import uniform
from numpy.random import randint

if len(sys.argv) < 2:
    print("Illegal number of arguments!")
    exit()

test_cases = int(sys.argv[1])

cmd_list = ['adta', 'adtd', 'adtq', 'adtr', 'adtp'] # adtreset and adtsort doensn't need to be checked frequently
cmd_prob = [0.35, 0.35, 0.05, 0.05, 0.2]
adt = []

max_strlen = 5

def get_random_str():
    return ''.join([chr(randint(97, 123)) for _ in range(1, max_strlen + 1)])

def get_adt_item():
    if uniform() < 0.2:
        return get_random_str()
    else:
        idx = randint(0, len(adt) + 1)
        if idx < len(adt):
            return adt[idx]
        else:
            return get_random_str()

def get_item_idx():
    bias = int(0.001 * len(adt))
    return randint(-bias, len(adt) + bias + 1)

def get_adtq_cmd():
    return 'adtq ' + get_adt_item()

def get_adtp_cmd():
    cmd = 'adtp'
    if uniform() < 0.3:
        cmd += ' -r'
    else:
        if uniform() < 0.5:
            cmd += (' ' + str(get_item_idx()))
    return cmd

def get_adta_cmd():
    cmd = 'adta'
    if uniform() < 0.2:
        s = get_random_str()
        cmd += (' -s ' + s)
        adt.append(s)
    else:
        n = 10 * randint(1, 100)
        cmd += (' -r ' + str(n))
        for _ in range(n):
            adt.append(get_random_str())
    return cmd

def get_adtd_cmd():
    cmd = 'adtd'
    opts = [' -a', ' -s', ' -r', ' -f', ' -b']
    opt_prob = [0.1, 0.1, 0.4, 0.2, 0.2]
    opt = np.random.choice(opts, p = opt_prob)
    if opt == ' -a':
        return cmd + opt
    elif opt == ' -s':
        return cmd + opt + ' ' + get_adt_item()
    else:
        return cmd + opt + ' ' + str(randint(1, int(1.001 * len(adt) + 2)))

def get_adtr_cmd():
    cmd = 'adtr'
    strlen = str(randint(1, 11))
    cmd += (' ' + strlen)
    max_strlen = strlen
    return cmd


dofile = ""
for _ in range(test_cases):
    cmd = np.random.choice(cmd_list, p = cmd_prob)
    if cmd == 'adta': 
        dofile += get_adta_cmd()
    elif cmd == 'adtd':
        dofile += get_adtd_cmd()
    elif cmd == 'adtq':
        dofile += get_adtq_cmd()
    elif cmd == 'adtr':
        dofile += get_adtr_cmd()
    else:
        dofile += get_adtp_cmd()
    dofile += '\n'
    if uniform() < 0.01:
        dofile += 'adts\n'

dofile += 'usage\n'
dofile += 'q -f\n'
with open("mydo", 'w') as file:
    file.write(dofile)
