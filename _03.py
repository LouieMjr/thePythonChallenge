import string
import re
import requests
from bs4 import BeautifulSoup, Comment


response = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
soup = BeautifulSoup(response.text, 'html.parser')

comment = (soup.find_all(string=lambda text: isinstance(text, Comment)))

match = re.findall("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", *comment) # unpack/spread array with *
print(match) # look at small letter in each of the given strings to makeup answer!