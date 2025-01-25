from requests import get 
from string import ascii_letters
from bs4 import BeautifulSoup, Comment

res = get("http://www.pythonchallenge.com/pc/def/ocr.html")

soup = BeautifulSoup(res.text, 'html.parser')

# print(type(soup))

rare = soup.find_all(string=lambda text: isinstance(text, Comment))[1]

print("".join([ele for ele in rare if ele in ascii_letters]))
