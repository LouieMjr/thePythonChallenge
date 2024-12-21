import string
import re
import requests
from bs4 import BeautifulSoup, Comment


response = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
soup = BeautifulSoup(response.text, 'html.parser')

comment = (soup.find_all(string=lambda text: isinstance(text, Comment)))

pattern = r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]"
match = "".join(re.findall(pattern, *comment)) # unpack/spread array with *
print(match) # look at small letter in each of the given strings to makeup answer!

# import re
# from stringfdf import ascii_lowercase as lowercase
# from requests import get

# response = get('http://www.pythonchallenge.com/pc/def/equality.html')

# response = str(response.text)
# pattern = r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"
# list_of_matches = re.findall(pattern, response)

# small_letters = ''
# for word in list_of_matches:
#   for i in range(1, len(word) - 2):
#     letter = word[i]
#     if letter in lowercase:
#       small_letters += letter