
def table(t):
	title = t.replace('Table','')
	table_d = {}
	table_d[title.split()[0]] = title.split(title.split()[0])[-1]
	t_ = [i for i in t[1:] if i != '']
	x = t_[0].split()
	y = []
	for i in t_[1:]:
		y.append(i.split()[0])	
	new_tb = t_[1:]
	first_line = t_[0]
	for i in x:
		b,e = find_index(first_line,i)
		for j in range(len(y)):
			if new_tb[j][b:e] != '':
				element = forward(new_tb[j][b:]) + backward[j][:b]
				
			
					

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
#line t_[0][:12]
	w = ''
	for i in reversed(s):
		if not i.isspace():
			w += i
		else:
			break
	
