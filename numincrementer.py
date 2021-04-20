file = open('num.txt', 'r')

num = file.read()
num = int(num)
num += 1
num = str(num)
file.close()

file = open('num.txt', 'w')
file.write(num)
file.close()
