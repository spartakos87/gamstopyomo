from find_parenthesis import find_parenthesis as fp
from find_slashes import find_slashes as fs


"""
Manipulate lines like this, a     age of trees    / a01*a24 /
This function must return the variable,a
The comment of it , age of trees
And values of it , which there are between slashes,a01*a24
But in case like that,mc(m) cutting months  / jul, aug, sep, oct /
We take and value between () , the m
"""

def manipulate_lines(text):
	name_fun = ''
	contain_par = ''
	contain_sla = ''
	comm = ''
	text = text.strip()
	# First find the function, for example mc(m)
	func = text[:text.find(' ')]
	# Check if there are (), if find what they include
	if func.find('(') != -1:
		contain_par = fp(func)
		name_fun = func.split('(')[0]
	else:
		name_fun = func
	# Check if there are // , if find what they include
	if text.find('/') != -1:
		contain_sla = fs(text)
	# Find the comments of function
	comm = text.split(func)[-1]
	if comm.find('/') != -1:
		comm = comm.split('/')[0].strip()
	# Return dictionary with all values , even if are empty
	d = {}
	d['functio_name'] = name_fun
	d['comments'] = comm
	d['slashes'] = contain_sla
	d['parenthesis'] = contain_par
	return d
