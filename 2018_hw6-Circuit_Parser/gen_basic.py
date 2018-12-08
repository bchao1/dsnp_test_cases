import os
import sys

aag_dir = './aag_test'
do_dir = './dofiles'

aag_files = os.listdir(aag_dir)
for f in aag_files:
    s = ""
    s += ("cirread " + os.path.join(aag_dir, f) + '\n')

    s += "cirp -s\n"
    s += "cirp -n\n"
    s += "cirp -pi\n"
    s += "cirp -po\n"
    s += "cirp -fl\n"
    s += "cirwrite\n"

    s += "q -f\n"
    with open(os.path.join(do_dir, f + '-do'), 'w') as out:
        out.write(s)
