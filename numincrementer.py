file = open('num.txt', 'r')

num = file.read()
num = int(num)
print(num)
num += 1
print(num)
num = str(num)
print(num)
file.close()

file = open('num.txt', 'w')
file.write(num)
print(num)
file.close()
