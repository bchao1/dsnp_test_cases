import os
import sys

aag_dir = './aag_files'
do_dir = './basic_dofiles'
out_dir = './basic_outputs'

if not os.path.exists(do_dir):
	os.mkdir(do_dir)
if not os.path.exists(os.path.join(out_dir, 'mine')):
	os.makedirs(os.path.join(out_dir, 'mine'))
if not os.path.exists(os.path.join(out_dir, 'ref')):
	os.makedirs(os.path.join(out_dir, 'ref'))

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

	s += "usage\n"
	s += "q -f\n"
	with open(os.path.join(do_dir, f + '-do'), 'w') as out:
		out.write(s)
