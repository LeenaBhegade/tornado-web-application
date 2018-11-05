from collections import Counter
from operator import itemgetter
import re

from bs4.element import Comment
from bs4 import BeautifulSoup
import requests

def validate_tag(element):
	if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
		return False
	if isinstance(element, Comment):
		return False
	return True

def build_word_dict(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	data = soup.findAll(text=True)
	texts = filter(validate_tag, data)
	text = u" ".join(t.strip().replace("'", "") for t in texts)
	wordArray = re.findall(r"[\w']+", text)
	newArray = [element for element in wordArray if len(element) > 3]
	return Counter(newArray).most_common(100)
