# Importando TKinter

from ctypes.wintypes import LARGE_INTEGER
from email.mime import image
from msilib.schema import ListBox
from tkinter import *

#Importando Fonte

from pyglet import font
font.add_file('Bangers.ttf')
#action_man = font.load('wwDigital.ttf')

#Importando pillow

from PIL import Image, ImageTk

#Importando pygame som

import pygame
from pygame import mixer

import os

# Cores 

cor0 = '#f0f3f5' #Cinza
cor1 = '#feffff' #Branco
cor2 = '#3fb5a3' #Verde
cor3 = '#2e2d2c' #Preto
cor4 = '#403d3d' #Preto
cor5 = '#4a88e8' #Azul 


#Criando Janela 

janela = Tk()
janela.title('🔊 Player By WeLL 🔊')
janela.geometry('352x255')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)



#Frames

frame_es = Frame(janela,width=150,height=150,bg=cor3)
frame_es.grid(row=0,column=0,pady=1,padx=1,sticky=NSEW)

frame_di = Frame(janela,width=250,height=150,bg=cor3)
frame_di.grid(row=0,column=1,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=404,height=100,bg=cor3)
frame_baixo.grid(row=1,column=0,columnspan=3,pady=1,padx=0,sticky=NSEW)


# Config o frame esquerda

image_1 = Image.open('icon1.png')
image_1 = image_1.resize((120,120))
image_1 = ImageTk.PhotoImage(image_1)

label_logo = Label(frame_es, width=130,image=image_1, compound=LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=cor3, fg=cor3,)
label_logo.place(x=24,y=15)


#Criando funções

# Tocar musica
def play_musica():
    rodan= listbox.get(ACTIVE)
    label_play['text'] = rodan
    mixer.music.load(rodan)
    mixer.music.play()

# Def Pause | Pausar Musica
def pause_musica():

    mixer.music.pause()

# Continuar musica
def conti_musica():
    mixer.music.unpause()

#Parar a Musica

def parar_musica():
    mixer.music.stop()

# Proxima musica

def proxi_musica():
    tocando = label_play['text']
    index = muiscas.index(tocando)
    novo_index = index + 1
    tocando = muiscas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

# Deletar os elementos na playlist
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_play['text'] = tocando

# Musica Anterior 
    
def anterior_musica():
    tocando = label_play['text']
    index = muiscas.index(tocando)
    novo_index = index - 1
    tocando = muiscas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

# Deletar os elementos na playlist
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_play['text'] = tocando
    



# Config o frame direita

#lista = ['Welson','test','Test','Welson','test','Test','Welson','test','Test','Welson','test','Test',]

listbox = Listbox(frame_di,width=22, height=10, selectmode=SINGLE, font=('Bangers 11 '),bg= cor3,fg=cor1 )
listbox.grid(row=0, column=0)

s = Scrollbar(frame_di)
s.grid(row=0,column=1,sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)



#COnfig Frame baixo 

label_play = Label(frame_baixo, text='🎵🎵 Escolha sua Música 🎵🎵 ', width=44,justify=CENTER,anchor='s',font=('Bangers 14 '),bg=cor3,fg=cor1)
label_play.place(x=0,y=0)


#COnfig Frame Botão

image_2 = Image.open('2.png')
image_2 = image_2.resize((30,30))
image_2 = ImageTk.PhotoImage(image_2)
b_ante = Button(frame_baixo,command=anterior_musica, width=35,height=35,image=image_2,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=cor3,fg=cor3)
b_ante.place(x=38,y=35)

image_3 = Image.open('3.png')
image_3 = image_3.resize((30,30))
image_3 = ImageTk.PhotoImage(image_3)
b_play = Button(frame_baixo,command=play_musica, width=35,height=35,image=image_3,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=cor3,fg=cor3)
b_play.place(x=84,y=35)

image_4 = Image.open('4.png')
image_4 = image_4.resize((30,30))
image_4 = ImageTk.PhotoImage(image_4)
b_avan2 = Button(frame_baixo,command=proxi_musica,width=35,height=35,image=image_4,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=cor3,fg=cor3)
b_avan2.place(x=130,y=35)

image_5 = Image.open('5.png')
image_5 = image_5.resize((30,30))
image_5 = ImageTk.PhotoImage(image_5)
b_pause = Button(frame_baixo,command=pause_musica,width=35,height=35,image=image_5,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=cor3,fg=cor3)
b_pause.place(x=176,y=35)

image_6 = Image.open('6.png')
image_6 = image_6.resize((30,30))
image_6 = ImageTk.PhotoImage(image_6)
b_avan2 = Button(frame_baixo,command=conti_musica,width=35,height=35,image=image_6,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=cor3,fg=cor3)
b_avan2.place(x=222,y=35)

image_7 = Image.open('7.png')
image_7 = image_7.resize((30,30))
image_7 = ImageTk.PhotoImage(image_7)
b_ante = Button(frame_baixo,command=parar_musica,width=35,height=35,image=image_7,font=('ivy 10 bold'),relief=RAISED,overrelief=RIDGE,bg=cor3,fg=cor3)
b_ante.place(x=268,y=35)


#Função carregar musica

os.chdir(r'C:\Users\LENOVO\Desktop\musica')
muiscas = os.listdir()

def mostrar():
    for i in muiscas:
        listbox.insert(END,i)    


mostrar()

# Inciar o mixer
mixer.init()

janela.mainloop()