
def init_list(text):
	ch = ''
	ch = [i for i in text if i.isalpha()]
	if len(ch) > 0 :
		ch = ch[0]
		text = text.replace(ch,'')
	text = text.split('*')
	b = text[0]
	e = text[1]
	lista =[]
	for i in range(int(b),int(e)+1):
		if i < 10:
			lista.append(ch+'0'+str(i))
		else:
			lista.append(ch+str(i))
	return lista
	

