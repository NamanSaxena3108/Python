path = r'F:\coding\python\projects\py.jpeg'

key = int(input('Enter key for encryption of image: '))

print('The path of the file:', path)
print('The key for encryption:', key)

with open(path, 'rb') as fin:
    image = bytearray(fin.read())

for index, value in enumerate(image):
    image[index] = value ^ key

with open(path, 'wb') as fout:
    fout.write(image)

print('Encryption done.')