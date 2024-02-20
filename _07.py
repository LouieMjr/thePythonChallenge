from PIL import Image, ImageColor
from collections import Counter

# from urllib.request import urlopen
# url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
# img = Image.open(urlopen(url))


img = Image.open('oxygen.png')
# print(img.show())
# print(img.size)
# left, upper, right, lower
box = (0, 45, 608, 50)
# print(img.show())
gray_cropped_line = img.crop(box)
# print(gray_cropped_line.size)
# print(gray_cropped_line.show())


# colors = Counter(gray_cropped_line.getdata())    # dict: color -> number

list_of_RGBvalues = list(gray_cropped_line.getdata())
list_of_Unique_RGBvalues = set(gray_cropped_line.getdata())

newlist = []
newlist1 = []

for RGBvalue in list_of_RGBvalues:
  if(chr(RGBvalue[0]) not in newlist):
    newlist.append(chr(RGBvalue[0]))
    # print(RGBvalue, RGBvalue[0], chr(RGBvalue[0]))
  
print(''.join(newlist))

for x in newlist:
  if ord(x) not in newlist1:



# set(colors)                  # set of unique colors  
# len(colors)                  # number of unique colors 
# colors[(0, 0, 0)]            # black color frequency
# newImg = max(colors, key=colors.get)  # most frequent color
# print(newImg)