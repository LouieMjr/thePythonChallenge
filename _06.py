import urllib.request
import zipfile
from io import BytesIO


filenum = "90052"

def next_File(txt_filenum, collect_comments = []):

    z = zipfile.ZipFile('channel.zip')

    if txt_filenum.isdigit():
        filename = txt_filenum + '.txt'
        comment = z.getinfo(filename).comment.decode('utf-8')  # Decode bytes to str
        collect_comments.append(comment)
        info = z.read(filename).decode('utf-8')
        txt_filenum = info.split()[-1]
        next_File(txt_filenum, collect_comments)
    
    collected = ''.join(collect_comments)
    z.close()
    return collected

# print(next_File(filenum))

###--------------------------------------------------------------------------------------###

url = "http://pythonchallenge.com/pc/def/channel.zip"
zobj = BytesIO()

response_bytes = urllib.request.urlopen(url).read()
zobj.write(response_bytes)

z = zipfile.ZipFile(zobj) # didnt have to download the zip file locally
# z = zipfile.ZipFile('channel.zip') # with zipfile downloaded locally

collected_comments = []

while True:
    if filenum.isdigit():
        filename = filenum + '.txt'
        comment = z.getinfo(filename).comment.decode('utf-8')  # Decode bytes to str
        collected_comments.append(comment)
        # info = z.read(filename)
        # filenum = info.split(b' ')[-1].decode('utf-8')
        info = z.read(filename).decode('utf-8')
        filenum = info.split()[-1] # looks cleaner than above, if you decode first after reading
    else:
        break

z.close()
print(''.join(collected_comments))