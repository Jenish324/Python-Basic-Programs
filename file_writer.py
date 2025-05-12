file = open('sample.txt', 'r+')

data = file.read()

print(data)

file.write('\nsomething new here to write')

file.close()