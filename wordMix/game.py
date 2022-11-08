from ast import For
from difflib import Match
import random
import os
from tkinter import *      

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

#ws.configure(bg='black')
canvas = Canvas(ws,width = 512, height = 512)

canvas.pack()      
img = PhotoImage(file='logo.png') 
canvas.place(x=0,y=0)     
canvas.create_image(
    0,
    0,
    anchor=NW, 
    image=img
    )      
ws.mainloop()  
"""while(True):
    answ=input('введите сложность 1.легко 2.сложно ')
    match answ:
        case "1":
            file = open('Words.txt',encoding='utf-8',mode="r")
        case "2":
            file = open('words1.txt',encoding='utf-8',mode="r")
            
    for i in range(random.randint(0,19)):
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
        answ=input('введите слово  ')
        if(answ==txt):
            print(f'вы угадали с {6-attempt}-й попытки')
            input('нажмите enter')
            break
            file.close()
        elif(attempt>1):
            print('попытайтесь ещё') 
            attempt-=1
            print(f'у вас осталось {attempt} попыток')
            input('нажмите enter')   
        else:
            print('вы не угадали')                 
            break
            file.close()"""
