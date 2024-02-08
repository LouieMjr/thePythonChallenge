import zipfile

myZip = 'spam.zip'

# Create a ZipFile and write 'yerrrrrrr' to 'eggs.txt'
with zipfile.ZipFile(myZip, 'w') as theZip:
    theZip.writestr('eggs/eggs.txt', 'this is from inside the txt file')
    # theZip.write('eggs/123.txt')

# Open the zip file again and set a comment for 'eggs.txt'
with zipfile.ZipFile(myZip, 'a') as theZip:
    # Set a comment for 'eggs.txt' within 'spam.zip'
    # comment_for_eggs = b'yooooooooooo'
    # theZip.writestr('eggs.txt', 'this is from inside the txt file')
    theZip.comment = b'yooooooooooo'

# Read and print the content of 'eggs.txt' and its comment
with zipfile.ZipFile(myZip, 'r') as theZip:
    file_content = theZip.read('eggs/eggs.txt').decode('utf-8')
    zip_comment_for_eggs = theZip.comment.decode('utf-8')

print(f"File Content from inside 'eggs.txt': {file_content}")
print(f"Zip Comment for 'eggs.txt' in 'spam.zip': {zip_comment_for_eggs}")
