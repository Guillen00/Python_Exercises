from tkinter import *
 
root = Tk()     
top = Frame(root)
top.pack()
 
label = Label(top, text='Entrada')
entry = Entry(top)
button = Button(top, text="Presioname")
 
label.pack()
entry.pack()
button.pack()
 
def onEnter(event):
    funcion()
 
def funcion():
    print (entry.get())
 
root.bind('<K_RIGHT>', onEnter)
button.config(command=funcion)
 
root.mainloop()
