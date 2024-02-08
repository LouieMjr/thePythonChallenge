import requests
from bs4 import BeautifulSoup


def getUrl(link):
  
  res = requests.get(link);
  pourSoup = BeautifulSoup(res.text, 'html.parser');
  return pourSoup;
  

def iterateThroughLinks(soup):
  
  numberFromString = '';
  for string in soup:
    for char in string:
      if char.isdigit():
        numberFromString += char;
    return numberFromString;



def iterate(howMany, func1, func2, num):
  for x in range(howMany):
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num}';
    insertSoup = func1(url)
    num = func2(insertSoup)
    print(num)

starting = '90052';
print(iterate(400, getUrl, iterateThroughLinks, starting))