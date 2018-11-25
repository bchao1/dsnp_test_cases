# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:02:33 2018

@author: USER
"""
import sys
import os
import numpy as np

if len(sys.argv) < 2:
    print("Invalid number of arguments!")
    exit()

test_cases = int(sys.argv[1])
json_dir = 'tests'
if not os.path.exists(json_dir):
    os.mkdir(json_dir)

# Define the commands and mandantory field length
commands = [
        ('dbappend', 4), # args : 2
        ('dbaverage', 4), # args : 0
        ('dbcount', 3), # args : 0
        ('dbmax', 4), # args : 0
        ('dbmin', 4), # args : 0
        ('dbprint', 3), # args (opt : 1)
        ('dbread', 3), # args : 1 (filename (.json))
        ('dbsort', 4), # args : 1 (key or value)
        ('dbsum', 4), # args : 0
        #('dofile', 2), # args : 1 (filename (dofile))
        ('help', 3), # args : 0
        ('history', 3)#, # args : 0
        #('quit', 1) # args (opt : 1)
        ]

no_arg_cmd = ['dbaverage', 'dbcount', 'dbmax', 'dbmin', 'dbsum', 'help', 'history']
json_files = ['../tests/test{}.json'.format(i) for i in range(1, 5)]
json_keys = []

def case_shuffle(cmd):
    char = list(cmd)
    char = [c.lower() if np.random.uniform() > 0.5 else c.upper() for c in char]
    return ''.join(char)

def partial_command(cmd, man_len, good = True):
    if man_len == 1:
        man_len += 1
    if good:
        end = np.random.randint(man_len - 1, len(cmd))
    else:
        end = np.random.randint(0, man_len - 1)
    return cmd[:end]

def good_command():
    num_commands = len(commands)
    if np.random.uniform() < 0.2:
        idx = 0
    else:
        idx = np.random.randint(1, num_commands)
    cmd = partial_command(commands[idx][0], commands[idx][1])
    cmd = case_shuffle(cmd)
    return cmd, commands[idx][0] # Returns shuffled cmd and original command

def bad_command():
    num_commands = len(commands)
    idx = np.random.randint(0, num_commands)
    good_cmd = partial_command(commands[idx][0], commands[idx][1])
    bad_cmd = partial_command(commands[idx][0], commands[idx][1], False)
    
    good_cmd = case_shuffle(good_cmd)
    bad_cmd = case_shuffle(bad_cmd)
    
    good_cmd += random_command(5)
    if np.random.uniform() > 0.5:
        bad_cmd += random_command(5)
    cmd = [good_cmd, bad_cmd, random_command(10)]
    np.random.shuffle(cmd)
    return cmd[0]

def random_command(max_len):
    cmd_len = np.random.randint(1, max_len)
    return ''.join([str(chr(np.random.randint(33, 127))) for _ in range(cmd_len)])

def gen_command():
    if np.random.uniform() < 0.8:
        return good_command()
    else:
        return bad_command()

def rand_arg(max_len):
    arg_len = np.random.randint(1, max_len)
    return ''.join([str(chr(np.random.randint(33, 127))) for _ in range(arg_len)])

def rand_key(max_len):
    arg_len = np.random.randint(1, max_len)
    key = ''.join([str(chr(np.random.randint(97, 123))) for _ in range(arg_len)])
    return case_shuffle(key)

def rand_int(bound):
    return str(np.random.randint(-bound, bound))

def json_gen(idx):
    n = np.random.randint(0, 1000)
    json_keys = []
    json_file = "{\n"
    while len(json_keys) != n:
        key = rand_key(10)
        if key not in json_keys:
            json_keys.append(key)
            json_file += ('  "' + key + '" : ' + str(np.random.randint(1000)))
            if len(json_keys) != n:
                json_file += ','
            json_file += '\n'
    json_file += '}\n'
    json_path = os.path.join(json_dir, "test{}.json".format(idx))
    with open(json_path, 'w') as file:
        file.write(json_file)
    return json_path

def gen_action():
    cmd = gen_command()
    if len(cmd) == 2:
        shuffled, orig = cmd
        action = shuffled
        if orig in no_arg_cmd:
            if np.random.uniform() < 0.2:
                action += (' ' + rand_arg(10))
            return action
        elif orig == 'dbappend':
            if np.random.uniform() < 0.7:
                if np.random.uniform() < 0.2 and len(json_keys) > 0:
                    key = json_keys[np.random.randint(0, len(json_keys))]
                else:
                    key = rand_key(10)
                action += (' ' + key + ' ' + rand_int(1000))
                if key not in json_keys:
                    json_keys.append(key)
            else:
                miss_arg = rand_key(10)
                bad_key = rand_arg(10) + ' ' + rand_int(1000)
                bad_value = rand_key(10) + ' ' + rand_arg(10)
                no_arg = ''
                candidates = [miss_arg, bad_key, bad_value, no_arg]
                np.random.shuffle(candidates)
                action += (' ' + candidates[0])
            
            return action
        
        elif orig == 'dbprint':
            if np.random.uniform() < 0.4:
                return action
            if np.random.uniform() < 0.9 and len(json_keys) > 0:
                key = case_shuffle(json_keys[np.random.randint(0, len(json_keys))])
            else:
                key = rand_key(10)
            return action + ' ' + key
        
        elif orig == 'dbsort':
            if np.random.uniform() < 0.2:
                if np.random.uniform() < 0.5:
                    action += (' ' + rand_arg(10))
                return action
            args = ['-k', '-v', '-keyzfsagdf' , '-valurewg', '-key', '-value']
            np.random.shuffle(args)
            return action + ' ' + args[0]
        elif orig == 'dbread':
            if np.random.uniform() < 0.2:
                action += ' -r '
            else:
                action += ' '
            np.random.shuffle(json_files)
            if np.random.uniform() < 0.2:
                action += rand_arg(10)
            else:
                action += json_files[0]
            return action
    else:
        return cmd
    
action = [gen_action() for _ in range(test_cases)]
json_files = [json_gen(i) for i in range(1, 11)]
np.random.shuffle(json_files)
action.insert(0, 'dbr ' + json_files[0])

while 'q' in action:
    action.remove('q')
action.append('q -f')

with open('mydo', 'w') as file:
    for line in action:
        if line is not None:
            file.write(line + '\n')