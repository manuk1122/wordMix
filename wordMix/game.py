from ast import For
from difflib import Match
import random
import os
from tkinter import *      
from PIL import Image





def CT ():
    file = open('Words.txt',encoding='utf-8',mode="r")
    ran=random.randint(1,18)            
    for i in range(ran):
        file.readline()
    txt=file.readline()
    txt = txt.replace('\n','')
    Word=txt.split()
    for i, word in enumerate(map(list,Word)):
        random.shuffle(word)
        Word[i]=''.join(word)
    lB['text']=Word
    lB1['text']=ran

def CT1 ():
    file = open('words1.txt',encoding='utf-8',mode="r")            
    for i in range(random.randint(1,9)):
        file.readline()
    txt=file.readline()
    txt = txt.replace('\n','')
    Word=txt.split()
    for i, word in enumerate(map(list,Word)):
        random.shuffle(word)
        Word[i]=''.join(word)
    lB['text']=Word

def getText():
    texT=text_box.get()
    lB1.configure(text=texT)

ws = Tk()
ws.title('PythonGuides')
ws.geometry('1920x1080')

ws.configure(bg='black')
canvas = Canvas(ws,width = 150, height = 150)
canvas.pack()      
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
    command=getText
)
 
button.pack()
button.place(x=1500,y=700)
#------------------------------------------------
text_box = Entry(ws,width=50)
text_box.pack()
text_box.place(x=810,y=700)
#сложность
rB1=Radiobutton(text='лёгкий',value=1,command=CT)
rB1.pack()
rB1.place(x=710,y=300)
rB2=Radiobutton(ws,text='средний',value=2,command=CT1)

rB2.pack()
rB2.place(x=710,y=340)
rB3=Radiobutton(ws,text='сложный',value=3)
rB3.pack()
rB3.place(x=710,y=380)
rB4=Radiobutton(ws,text='не пройдёш',value=4)
rB4.pack()
rB4.place(x=710,y=420)
lB=Label(text='hEllO',height=5,width=100,font=("Arial",14))
lB.pack()
lB.place(x=510,y=150)
lB1=Label(text='hEllO')
lB1.pack()
lB1.place(x=510,y=750)
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
