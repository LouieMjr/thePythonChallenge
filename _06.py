import urllib.request
import zipfile
from io import BytesIO

zobj = BytesIO()
zobj.write(urllib.request.urlopen("http://pythonchallenge.com/pc/def/channel.zip").read())
z = zipfile.ZipFile(zobj)

filenum = "90052"
lcomment = []

while True:
    if filenum.isdigit():
        filename = filenum + '.txt'
        comment = z.getinfo(filename).comment.decode('utf-8')  # Decode bytes to str
        print(comment)
        lcomment.append(comment)
        info = z.read(filename)
        filenum = info.split(b' ')[-1].decode('utf-8')
    else:
        break

z.close()
print(''.join(lcomment))