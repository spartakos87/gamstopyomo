ml=[]
def find_tags(ar):
	for k,i in enumerate(ar):
		l =[j for j in a if j in i]
		d={}
		if len(l)>0:
			u=[]
			u.append(k)
			d[l[0]]=u
			ml.append(d)
	 for i in range(len(ml)):
		if i != len(ml)-1:
			t=ml[i+1].values()[0][0]
			ml[i].values()[0].append(t)
#	return ml
	li = []
	for i in ml:
		d = {}
		text = ar[i.values()[0][0]:i.values()[0][-1]]
		d[i.keys()[0]]=text
		li.append(d)
	return li
