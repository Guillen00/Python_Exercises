from tkinter import *

def seleccionar():
    print(opcion.get())
    if monitor==1:
        print('ready')


# Configuración de la raíz
root = Tk()
root.minsize(400,400)
opcion = IntVar()

uno=PhotoImage(file='izquierda encendida.gif')
dos=PhotoImage(file='derecha encendida.gif')
Radiobutton(root, image=uno, variable=opcion, 
            value=1, command=seleccionar).place(x=0,y=0)
Radiobutton(root, text="OFF", variable=opcion, 
            value=2, command=seleccionar).place(x=120,y=16)
Radiobutton(root,image=dos, variable=opcion,   
            value=3, command=seleccionar).place(x=200,y=0)

monitor = Label(root)
monitor.pack()





# Finalmente bucle de la aplicación
root.mainloop()
