import numpy as np
cmd = ['mtn', 'mtd', 'mtp', 'mtr']
probs = ['0.35', '0.35', '0.25', '0.05']

rand = np.random.uniform

def rand_arg():
    return ''.join([chr(np.random.randint(65, 126)) for _ in range(int(5 * rand()))])

test = 1000

dofile = ""

obj_len = 1
arr_len = 0
for _ in range(test):
    line = np.random.choice(cmd, p = probs)
    if line == "mtn":
        if rand() > 0.1:
            if rand() > 0.1:
                if rand() > 0.9:
                    line += (' ' + rand_arg())
                else:
                    obj_num = np.random.randint(-100, 1000)
                    obj_len += obj_num
                    line += (' ' + str(obj_num))
            if rand() > 0.5:
                line += (' -a ' + str(np.random.randint(5, 200)))
            if rand() > 0.9:
                line += (' ' + rand_arg())
            
    elif line == "mtd":
        if rand() > 0.1:
            if rand() > 0.1:
                if rand() > 0.9:
                    line += (' ' + rand_arg())
                else:
                    if rand() > 0.5:
                        line += ' -i '
                    else: 
                        line += ' -r '
            if rand() > 0.9:
                line += (' ' + rand_arg())
            else:
                line += str(np.random.randint(-int(obj_len * 0.2), int(obj_len * 1.2)))
            if rand() > 0.5:
                line += ' -a'
            if rand() > 0.9:
                line += (' ' + rand_arg())

    elif line == "mtr":
        line += (' ' + str(np.random.randint(100, 5000) * 10))

    dofile += (line + '\n')

dofile += "q -f\n"
with open("mydo", 'w') as file:
    file.write(dofile)