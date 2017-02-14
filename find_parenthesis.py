import re

def find_parenthesis(text):
	text = re.findall('\(.*?\)',text)
#	text=text[0].replace('(','').replace(')','').strip()
	if len(text) > 0:
		text=text[0].replace('(','').replace(')','').strip()
		if text.find(',') != -1:
			text = text.split(',')
		return text

