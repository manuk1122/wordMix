from ast import For
from difflib import Match
import random
import os
from tkinter import *      
from PIL import Image
ws = Tk()
ws.title('PythonGuides')
ws.geometry('1920x1080')

ws.configure(bg='black')
canvas = Canvas(ws,width = 150, height = 150)
canvas.pack()      
img_new=Image.open('logo.png')
img_new1=img_new.resize((150,150)) 
img_new1.save('logo1.png')
img = PhotoImage(file='logo1.png')
canvas.place(x=0,y=0)     
canvas.create_image(
    0,
    0,
    anchor=NW, 
    image=img
    )      
#кнопка
button = Button(
    text="ввод!",
    width=25,
    height=5,
    bg="yellow",
    fg="black",
)
 
button.pack()
button.place(x=1500,y=700)
#------------------------------------------------
text_box = Text(
    width=50,
    height=5,
    bg="yellow",
    fg="black",
)
text_box.pack()
text_box.place(x=810,y=700) 
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
