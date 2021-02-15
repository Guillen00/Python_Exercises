import tkinter
from tkinter import *
import time
import threading
from WiFiClient import NodeMCU

def Ventana_Test_Driver():
    global estado, luces,vel,GAS,fre
    estado=1
    luces=1
    GAS=0
    fre=1
    W = NodeMCU()
    W.start()
    
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
    img2=PhotoImage(file='table.png')
    logo2=Label(root,image=img2,width=400,height=225).place(x=0,y=125)
    velocidad = StringVar()
    Label(root,textvariable=velocidad,font=("Verdana", 40, "bold")).place(x=425,y=20)
    velocidad.set(str(GAS)+"Km/h")
    img8=PhotoImage(file='emergencia.png')
    intermitentes = tkinter.Button(root, image=img8,command=lambda :thread_intermitentes(), width=100, height=100)
    intermitentes.place(x=450,y=250)
    img9=PhotoImage(file='Luz.png')
    luz = tkinter.Button(root, image=img9,command=lambda :thread_luz(), width=150, height=100)
    luz.place(x=550,y=250)
    img10=PhotoImage(file='mov.png')
    movimiento = tkinter.Button(root, image=img10,command=lambda :thread_especial(), width=100, height=100)
    movimiento.place(x=700,y=250)

    #Pedales
    img5=PhotoImage(file='gas1.gif')
    botongas = tkinter.Button(root, image=img5,command=lambda :thread_gas(),  width=100, height=200)
    botongas.place(x=270,y=470)
    img6=PhotoImage(file='freno1.gif')
    botonfreno = tkinter.Button(root, image=img6,command=lambda :thread_freno(), width=150, height=100)
    botonfreno.place(x=75,y=550)

    #informacion piloto
    a=Label(root, text=("Escuderia:"),justify=LEFT, font=("Arial", 15, "bold"))
    a.place(x=450,y=400)
    b=Label(root, text=("Piloto:"),justify=LEFT, font=("Arial", 15, "bold"))
    b.place(x=450,y=450)
    c=Label(root, text=("Nacionalidad:"),justify=LEFT, font=("Arial", 15, "bold"))
    c.place(x=450,y=500)

    #Bateria
    bat=PhotoImage(file='100.png')
    bate=Label(root,image=bat,width=100,height=100).place(x=780,y=0)
    def bat():
        bat=PhotoImage(file='100.png')
        bate=Label(root,image=bat,width=100,height=100).place(x=780,y=0)
        time.sleep(600)
        bat=PhotoImage(file='80.png')
        bate=Label(root,image=bat,width=100,height=100).place(x=780,y=0)
        time.sleep(600)
        bat=PhotoImage(file='60.png')
        bate=Label(root,image=bat,width=100,height=100).place(x=780,y=0)
        time.sleep(600)
        bat=PhotoImage(file='40.png')
        bate=Label(root,image=bat,width=100,height=100).place(x=780,y=0)
        time.sleep(600)
        bat=PhotoImage(file='20.png')
        bate=Label(root,image=bat,width=100,height=100).place(x=780,y=0)
        time.sleep(600)
    def thread_bateria():
        p=threading.Thread(target=bat)
        p.start()

        
    #sensor de luz
    sen=PhotoImage(file='com.png')
    sensor=Label(root,image=sen,width=100,height=100).place(x=780,y=125)


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
    
    
    def thread_especial():
        f=threading.Thread(target=send('zigzag;'))
        f.start()
    def thread_der():
        f=threading.Thread(target=send('derecha;'))
        f.start()
    def thread_izq():
        f=threading.Thread(target=send('izquierda;'))
        f.start()
    def thread_detener():
        f=threading.Thread(target=send('detener;'))
        f.start()
    def thread_avanzar():
        f=threading.Thread(target=send('avanzar;'))
        f.start()
        
    def izq():
        global img
        x=0
        send('dir-izq;')
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
        send('dir-der;')
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
        global img4,luces
        luces=luces+1
        
        while(luces%2==0):
            send('luz;')
            img4=PhotoImage(file='luz encendida.png')
            logo4=Label(root,image=img4,width=50,height=50).place(x=25,y=20)
            time.sleep(0.5)
        send('luz-off')      
        img4=PhotoImage(file='luz apagada.png')
        logo4=Label(root,image=img4,width=50,height=50).place(x=25,y=20)

            
    def thread_luz():
        p=threading.Thread(target=luz)
        p.start()
        f=threading.Thread(target=send('luz'))
        f.start()

    def intermitente():
        global img3
        global img
        x=0
        while(opcion.get()==2):
            send('parpadear;')
            img3=PhotoImage(file='derecha encendida.gif')
            logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
            img=PhotoImage(file='izquierda encendida.gif')
            logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            time.sleep(0.5)
            img3=PhotoImage(file='derecha apagada.gif')
            logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
            img=PhotoImage(file='izquierda apagada.gif')
            logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            time.sleep(0.5)
            x+=1
        
    def estado_emergencia():
        global img3
        global img
        global estado
        estado=estado+1

        

        while((estado%2==0)and (opcion.get()==2) ):
            send('parpadear;')
            img3=PhotoImage(file='derecha encendida.gif')
            logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
            img=PhotoImage(file='izquierda encendida.gif')
            logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            time.sleep(0.5)
            img3=PhotoImage(file='derecha apagada.gif')
            logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
            img=PhotoImage(file='izquierda apagada.gif')
            logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            time.sleep(0.5)

        img3=PhotoImage(file='derecha apagada.gif')
        logo3=Label(root,image=img3,width=50,height=50).place(x=225,y=20)
        img=PhotoImage(file='izquierda apagada.gif')
        logo=Label(root,image=img,width=50,height=50).place(x=125,y=20)
            
            
    def thread_intermitentes():
        d=threading.Thread(target=estado_emergencia)
        d.start()
    def volante_der(event):
        global img2
        thread_der()
        img2=PhotoImage(file='table_der.png')
        logo2=Label(root,image=img2,width=400,height=225).place(x=0,y=125)

    def volante_izq(event):
        global img2
        thread_izq()
        img2=PhotoImage(file='table_izq.png')
        logo2=Label(root,image=img2,width=400,height=225).place(x=0,y=125)
        
    def volante(event):
        global img2
        thread_detener()
        img2=PhotoImage(file='table.png')
        logo2=Label(root,image=img2,width=400,height=225).place(x=0,y=125)
    def gas():
        global GAS
        x=0
        thread_avanzar()
        while(x<6):
            GAS=GAS+20
            velocidad.set(str(GAS)+"Km/h")
            time.sleep(0.25)
            x+=1
    def thread_gas():
        d=threading.Thread(target=gas)
        d.start()

        
    def freno():
        global GAS,fre
        fre=+1
        if(fre%2==0):
            while(GAS<61):
                velocidad.set(str(GAS)+"Km/h")
                GAS=GAS+20
                time.sleep(0.25)
                print(GAS)
            
        
        else:
            while(GAS>-1):
                velocidad.set(str(GAS)+"Km/h")
                GAS=GAS-20
                time.sleep(0.25)
                print(GAS)
        
            GAS=GAS+20
    def thread_freno():
        d=threading.Thread(target=freno)
        d.start()
        f=threading.Thread(target=send('atras'))
        f.start()
    def send(comando):
        x=0
        while(x<1):
            mns=str(comando)
            W.send(mns)
            print("Envianto mensaje:",comando)
            x+=1
            
    #Teclado volante
    root.bind('<a>', volante_der)
    root.bind('<d>', volante_izq)
    root.bind('<w>',thread_gas)
    root.bind('<s>',volante)

    root.mainloop() 

    
    
Ventana_Test_Driver()

    
