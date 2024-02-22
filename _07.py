from PIL import Image, ImageColor
from collections import Counter
# from urllib.request import urlopen

# url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
# img = Image.open(urlopen(url))

img = Image.open('oxygen.png')
y = 48
end = 607
step = 7
pixel_count = []

for x in range(0, end, step):
  # print(img.getpixel((x, y))[0])
  pixel_count.append(chr(img.getpixel((x, y))[0]))
  
# print(pixel_count)
string = ''.join(pixel_count)
slicedstr = string[-44:-1]
arrayofString = slicedstr.split(', ')

arrayofString = [chr(int(value)) for value in arrayofString]
print(''.join(arrayofString))