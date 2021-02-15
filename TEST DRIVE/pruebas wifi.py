import tkinter
from tkinter import *
import time
import threading
from WiFiClient import NodeMCU
W = NodeMCU()
W.start()
root = tkinter.Tk()
root.minsize(900,800)
root.resizable(width=NO,height=NO)
root.title('TEST DRIVER')
img9=PhotoImage(file='Luz.png')
luz = tkinter.Button(root, image=img9,command=lambda :thread_luz(), width=150, height=100)
luz.place(x=550,y=250)

def thread_luz():
    p=threading.Thread(target=luz)
    p.start()
    f=threading.Thread(target=send('zigzag;'))
    f.start()
def send(comando):
        x=0
        while(x<1):
            mns=str(comando)
            W.send(mns)
            print("Envianto mensaje:",comando)
            x+=1
