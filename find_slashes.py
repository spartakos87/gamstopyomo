#re.findall('/.*?/', set[2])[0].replace('/','').strip()
import re
from init_list import init_list as il

def find_slashes(text):
	text = re.findall('/.*?/', text)
	#[0].replace('/','').strip()
	if len(text) > 0:
		text = text[0].replace('/','').strip()
		if text.find(',') != -1:
			text = text.split(',')
		if text.find('*') != -1:
			text = il(text)
		return text
