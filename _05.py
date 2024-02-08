from requests import get
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

raw = get(url)

# open file in binary write mode
with open('banner.p', 'wb') as file:
   file.write(raw.content)

# file = open('banner.p', 'w')
# # print(type(raw.text))
# # print(type(raw.content))
# file.write(raw.text)
# file.close()

# load file
pickled = pickle.load(open('banner.p', 'rb'))

for x in pickled:
   print(''.join([key * value for key, value in x]))
