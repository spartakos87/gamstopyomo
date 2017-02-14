from collections import OrderedDict

"""
Insert table as dictionary so we must take first the key Table

"""

def table(t):
#	extract_table = {}
	# Dictionary is ordered as we input the data
	extract_table = OrderedDict()
	t = t['Table']
	title = t[0].replace('Table','')
	table_d = {}
	# This dict include the name and comments of table
	table_d[title.split()[0]] = title.split(title.split()[0])[-1]
	t_ = [i for i in t[1:] if i != '']
	x = t_[0].split() # Columns
	y = [] # Lines
	for i in t_[1:]:
		y.append(i.split()[0])	
	new_tb = t_[1:]
	first_line = t_[0]
	for i in x:
		b,e = find_index(first_line,i)
		for j in range(len(y)):
			if new_tb[j][b:e] != '':
				fo = forward(new_tb[j][b:]) 
				ba = backward(new_tb[j][:b])
				element = ba + fo
			else:
				element = ''
			extract_table[(y[j],i)] = element
	# Return a dictionary with in tuple which first element is
	# the line and second element the column
	# and the value is the value..		
	return extract_table
					

def find_index(line,word):
	b = line.index(word)
	e = b+len(word)
	return b,e
""" 
def table_ele(t,y):
	for i in range(len(t)):
		for j in y:
			if j in t[i]:
				t[i] = t[i].replace(j,'')
	return t
"""

def forward(line):
#line t_[0][12:]
	w = ''
	for i in line:
		if not i.isspace():
			w +=i
		else:
			break
	return w

def backward(line):
	w = ''
	for i in reversed(line):
		if not i.isspace():
			w += i
		else:
			break
	return w
