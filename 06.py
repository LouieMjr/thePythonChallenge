from requests import get
import pickle


url = "http://www.pythonchallenge.com/pc/def/banner.p"

raw = get(url)

file = open('banner.p', 'w')
# print(type(raw.text))
# print(type(raw.content))
file.write(raw.text)
file.close()

pickled = pickle.load(open('banner.p', 'rb'))

for x in pickled:
   print(''.join([key * value for key, value in x]))
