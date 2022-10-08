file = open('Words.txt','r')
#print(*file)
#print(file)
#for i in range(5):
 #   print(file.read(i))
with open("Words.txt") as file:
    print(file.readline(1))
    print(file.readline(1))
    print(file.readline(1))
    print(file.readline(1))
    print(file.readline(1))
    print(file.readline(1))
file.close()
