"""
Find the equations inside gams file

"""
def find_equations(line):
	if line.find('..') != -1:
		name_eq = line.split('..')[0].strip()
		eq = line.split('..')[1].strip()
