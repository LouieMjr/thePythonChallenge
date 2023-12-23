import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345');

soup = BeautifulSoup(res.text, 'html.parser');

numberFromString = '';

for x in range(0, 401):
  for string in soup:
    for char in string:
      if char.isdigit():
        numberFromString += char;

    print(numberFromString);
    res = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={numberFromString}");
    soup = BeautifulSoup(res.text, 'html.parser');
    numberFromString = '';