# Insert gams file and extract comments
#com =ar.split('$Offtext')[0].replace('$Title','').replace('$Ontext','').split('\n')
#com = [i.strip()for i in com if i!='']
def comments(comm,pyfile):
	pyfile.write('""" \n')i
	for i in comm:
		pyfile.write(i + '\n')
	pyfile.write('"""\n ')
