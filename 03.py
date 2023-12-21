import requests
from bs4 import BeautifulSoup, Comment


res = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

soup = BeautifulSoup(res.text, 'html.parser')

rare = soup.find_all(string=lambda text: isinstance(text, Comment))

print(rare)
countObj = {};
newtxt = '';


for element in rare[1]:
  for symbol in element:
    if symbol in countObj:
      countObj[symbol] += 1;
    else:
      countObj[symbol] = 1;

print(countObj);

for symbol in countObj:
  if countObj[symbol] == 1:
    newtxt += symbol;

print(newtxt);