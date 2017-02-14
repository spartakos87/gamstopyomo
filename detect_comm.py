"""
Detect comments:
	If setence start with $ or * is comment
Insert line by line and check if is comment
"""

def detect_comm(text):
	comm = ''
	for i in text:
		if len(i) > 0:
			if i.strip()[0] == '$':
				comm = '#'+str(i.split('$')[-1])
			elif i.strip()[0] == '*':
				comm = '#'+str(i.split('*')[-1])
	return comm
