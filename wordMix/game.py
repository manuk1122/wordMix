from ast import For
import random
import os
file = open('Words.txt',encoding='utf-8',mode="r")
for i in range(random.randint(0,3)):
    file.readline()
txt=file.readline()
txt = txt.replace('\n','')
Word=txt.split()
for i, word in enumerate(map(list,Word)):
    random.shuffle(word)
    Word[i]=''.join(word)
attempt=5
while(True):
    os.system('cls||clear')
    print(Word)
    answ=input('введите слово')
    if(answ==txt):
        print('вы угадали')
        breaк
    else:
        print('вы не угадали')                 
        break
