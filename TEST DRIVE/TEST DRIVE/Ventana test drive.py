import tkinter
from tkinter import *
import time
import threading

def Ventana_Test_Driver():
    root = tkinter.Tk()
    root.minsize(900,800)
    root.resizable(width=NO,height=NO)
    root.title('TEST DRIVER')
    boton = tkinter.Button(root,text="Volver a la Página principal")
    boton.place(x=270,y=710)
    img=PhotoImage(file='izquierda apagada.gif')
    logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
    img3=PhotoImage(file='derecha apagada.gif')
    logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
    img4=PhotoImage(file='luz apagada.png')
    logo4=Label(root,image=img4,width=50,height=50).place(x=25,y=20)
    img2=PhotoImage(file='volante1.png')
    logo2=Label(root,image=img2,width=425,height=425).place(x=0,y=75)
    img5=PhotoImage(file='gas1.gif')
    botongas = tkinter.Button(root, image=img5, width=100, height=200)
    botongas.place(x=270,y=470)
    img6=PhotoImage(file='freno1.gif')
    botonfreno = tkinter.Button(root, image=img6, width=150, height=100)
    botonfreno.place(x=75,y=550)
    velocidad = StringVar()
    Label(root,textvariable=velocidad,font=("Verdana", 40, "bold")).place(x=425,y=20)
    velocidad.set("0 Km/h")
    img8=PhotoImage(file='emergencia.png')
    intermitentes = tkinter.Button(root, image=img8,command=lambda :thread_intermitentes(), width=100, height=100)
    intermitentes.place(x=450,y=250)
    img9=PhotoImage(file='Luces.png')
    luz = tkinter.Button(root, image=img9,command=lambda :thread_luz(), width=150, height=100)
    luz.place(x=550,y=250)

    def seleccionar():
        if (opcion.get()==3):
            thread_derecha()

        if (opcion.get()==1):
            thread_izquierda()
        
        

    opcion = IntVar()

    uno=PhotoImage(file='izquierda encendida.gif')
    dos=PhotoImage(file='derecha encendida.gif')
    Radiobutton(root, image=uno, variable=opcion, 
        value=1, command=seleccionar).place(x=450,y=150)
    Radiobutton(root, text="OFF", variable=opcion, 
        value=2, command=seleccionar).place(x=535,y=167)
    Radiobutton(root,image=dos, variable=opcion,   
        value=3, command=seleccionar).place(x=600,y=150)

    monitor = Label(root)
    monitor.pack()   
    
    
    def izq():
        global img
        x=0
        while((opcion.get())==1):
            img=PhotoImage(file='izquierda encendida.gif')
            logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            time.sleep(0.5)
            img=PhotoImage(file='izquierda apagada.gif')
            logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            time.sleep(0.5)
            x+=1
        
    def thread_izquierda():
        p=threading.Thread(target=izq)
        p.start()

    def der():
        global img3
        x=0
        while(opcion.get()==3):
            img3=PhotoImage(file='derecha encendida.gif')
            logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
            time.sleep(0.5)
            img3=PhotoImage(file='derecha apagada.gif')
            logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
            time.sleep(0.5)
            x+=1
        
    def thread_derecha():
        p=threading.Thread(target=der)
        p.start()

    def luz():
        global img4
        x=0
        while(x<6):
            img4=PhotoImage(file='luz encendida.png')
            logo4=Label(root,image=img4,width=50,height=50).place(x=25,y=20)
            time.sleep(1)
            x+=1
            img4=PhotoImage(file='luz apagada.png')
            logo4=Label(root,image=img4,width=50,height=50).place(x=25,y=20)

            
    def thread_luz():
        p=threading.Thread(target=luz)
        p.start()
    def thread_intermitentes():
        d=threading.Thread(target=der)
        i=threading.Thread(target=izq)
        d.start()
        i.start()
    root.mainloop() 

    
    
Ventana_Test_Driver()

    
