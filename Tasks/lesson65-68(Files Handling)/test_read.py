my_file = open('/home/khalid/Abolftoh/courses/Elzero python/Tasks/lesson65-68(Files Handling)/khalid.txt','r')


print(my_file.readline())
print(my_file.readline())
print(my_file.readline(10))

for line in my_file:
    print(line)
    if line.startswith('5'):
        break

my_file.close()