import string

strr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# txt = string.ascii_lowercase
# print(txt.find('a'))
newtxt = ''

for letter in string.ascii_lowercase:
  found = string.ascii_lowercase.find(letter)
    # if(found == -1):
    #   newtxt += '';
  index = found + 2
  if(index >= 26):
    newtxt += string.ascii_lowercase[index - found]
  else:
    newtxt += string.ascii_lowercase[index];


print(newtxt)

map = str.maketrans(string.ascii_lowercase, 'cdefghijklmnopqrstuvwxyzcc')

print('map'.translate(map))