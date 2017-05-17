
def hello():
    print('Hola mundo')

from tkinter import *
tk = Tk()
btn = Button(tk, text = "Click me", command = hello)
btn.pack()