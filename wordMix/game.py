from ast import For
from difflib import Match
import random
import os
import tkinter as  tk      

ws = tk.Tk()
ws.title('PythonGuides')
ws.geometry('500x500')


label = tk.Label(
    text="Привет, Tkinter!",
    foreground="white",  # Устанавливает белый текст
    background="black"  # Устанавливает черный фон
)
label.pack()





button = tk.Button(
    text="Нажми на меня!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
 
button.pack()

canvas = tk.Canvas(
    ws,
    width = 12, 
    height = 12
    )      
canvas.pack()      

img = tk.PhotoImage(file='unnamed.png')      
canvas.create_image(
    10,
    10, 
    anchor= tk.NW, 
    image=img
    )      
canvas.place(x =0,y=0)
ws.mainloop()  
"""
while(True):
    answ=input('введите сложность 1.легко 2.сложно ')
    match answ:
        case "1":
            file = open('Words.txt',encoding='utf-8',mode="r")
        case "2":
            file = open('words1.txt',encoding='utf-8',mode="r")
            
    for i in range(random.randint(0,19)):
       # print(i)
        file.readline()
    txt=file.readline()
    txt = txt.replace('\n','')
    Word=txt.split()
    for i, word in enumerate(map(list,Word)):
        random.shuffle(word)
        Word[i]=''.join(word)
    attempt=5
    while(True):
        #os.system('cls||clear')
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
            file.close()
"""