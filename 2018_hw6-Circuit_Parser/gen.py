import os
import sys
import numpy as np
from numpy.random import randint

if len(sys.argv) != 3:
    print("Invalid number of arguments!")
    print("Usage: python3 <aag file> <test cases>")
    exit()

aag_dir = './aag_files'
aag_file = os.path.join(aag_dir, sys.argv[1])

total_gates = 0
max_levels = 20
num_test = int(sys.argv[2])

with open(aag_file, 'r') as file:
    header = file.readline().strip().split(' ')
    total_gates = int(header[1]) + int(header[4])

dofile = ""
dofile += "cirread {}\n".format(aag_file)
dofile += "cirp -n\n"
dofile += "cirp -pi\n"
dofile += "cirp -po\n"
dofile += "cirp -fl\n"
dofile += "cirwrite\n"

for _ in range(0, num_test):
    fan_type = 'fanin' #if np.random.uniform() > 0.5 else 'fanout'
    dofile += "cirgate {} -{} {}\n".format(randint(0, total_gates), fan_type, randint(0, max_levels))

dofile += "usage\n"
dofile += 'q -f\n'

with open('mydo', 'w') as f:
    f.write(dofile)