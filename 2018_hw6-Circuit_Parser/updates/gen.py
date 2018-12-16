import os 
import sys
import copy
import numpy as np
import numpy.random as random
from numpy.random import randint

def get_prob(levels, base):
    base = float(base)
    l = np.arange(0, levels)
    p = base ** l
    return p / np.sum(p)

def get_gate_ids(max_id):
    gate_ids = list(range(1, max_id + 1))
    np.random.shuffle(gate_ids)
    return gate_ids

def construct_circuit(levels, level_gates, p_base):
    circuit = [[] for _ in range(randint(*levels) + 1)]

    pi_n, aig_n = 0, 0
    for i in range(len(circuit)):
        num_gates = randint(*level_gates)
        if i == 0:
            pi_n = num_gates
        else:
            aig_n += num_gates
        for _ in range(num_gates):
            circuit[i].append(gate_ids.pop())

    po_list = []
    output_prob = get_prob(len(circuit), p_base)
    for i in range(len(circuit)):
        if i == len(circuit) - 1:
            for g in circuit[i]:
                gate_id = 2 * g
                if random.uniform() > 0.5:
                    gate_id += 1
                po_list.append(gate_id)
        else:
            if random.uniform() < output_prob[i]:
                gates = copy.copy(circuit[i])
                random.shuffle(gates)
                out_num = randint(len(gates))
                for j in range(out_num):
                    gate_id = 2 * gates[j]
                    if random.uniform() > 0.5:
                        gate_id += 1
                    po_list.append(gate_id)
    circuit += [po_list]
    return circuit, (max_id, pi_n, 0, len(po_list), aig_n)

def gen_aag(circuit, header, p_base):
    aag_file = "aag {} {} {} {} {}\n".format(*header)
    for g in circuit[0]:
        aag_file += "{}\n".format(2 * g)
    for g in circuit[-1]:
        aag_file += "{}\n".format(g)
    for i in range(1, len(circuit) - 1):
        for g in circuit[i]:
            aag_file += "{}".format(2 * g)
            for _ in range(2):
                input_level = random.choice(range(i), p = get_prob(i, p_base))
                input = 2 * random.choice(circuit[input_level])
                if random.uniform() > 0.5:
                    input += 1
                aag_file += " {}".format(input)
            aag_file += '\n'

    with open('test.aag', 'w') as file:
        file.write(aag_file)

def gen_dofile(circuit, num_test):
    dofile = ""
    all_gates = sum(circuit, [])

    dofile += "cirr test.aag\n"
    dofile += "cirp -s\n"
    dofile += "cirp -n\n"
    dofile += "cirp -pi\n"
    dofile += "cirp -po\n"
    dofile += "cirp -fl\n"
    dofile += "cirwrite\n"

    for _ in range(0, num_test):
        fan_type = 'fanin' if random.uniform() > 0.5 else 'fanout'
        gate_id = random.randint(len(all_gates))
        dofile += "cirgate {} -{} {}\n".format(all_gates[gate_id], fan_type, randint(0, len(circuit)))
    dofile += "usage\nq -f\n"
    with open('mydo', 'w') as file:
        file.write(dofile)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Invalid number of arguments!")
		exit()
    # Configs
    p_base = random.uniform(1, 3) # Determines the "flattness" of the circuit
    max_id = 500 # Maximum gate id
    levels = (49, 50) # Range of circuit levels
    level_gates = (10, 11) # Range of number of gates in each level
    num_test = int(sys.argv[1]) # Number of test cases

    gate_ids = get_gate_ids(max_id) # Randomized list of gate ids
    circuit, header = construct_circuit(levels, level_gates, p_base)
    gen_aag(circuit, header, p_base)
    gen_dofile(circuit, num_test)