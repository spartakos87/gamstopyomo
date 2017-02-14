#re.findall('/.*?/', set[2])[0].replace('/','').strip()
import re

def find_slashes(text):
	text = re.findall('/.*?/', set[2])[0].replace('/','').strip()
	if len(text) > 0:
		if len(text) == 1:
			text = text[0]
		else:
			if text.find(',') != -1:
				text = text.split(',')
	return text
