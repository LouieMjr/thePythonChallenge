from requests import get 
from string import ascii_letters
from bs4 import BeautifulSoup, Comment

res = get("http://www.pythonchallenge.com/pc/def/ocr.html")

soup = BeautifulSoup(res.text, 'html.parser')

# print(type(soup))

rare = soup.find_all(string=lambda text: isinstance(text, Comment))[1]

print("".join([ele for ele in rare if ele in ascii_letters]))

# countObj = {};
# newtxt = '';


# for element in rare[1]:
#   for symbol in element:
#     if symbol in countObj:
#       countObj[symbol] += 1;
#     else:
#       countObj[symbol] = 1;

# print(countObj);

# for symbol in countObj:
#   if countObj[symbol] == 1:
#     newtxt += symbol;

# print(newtxt);