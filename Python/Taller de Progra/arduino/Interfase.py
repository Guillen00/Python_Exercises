# Importacion de bibliotecas
from tkinter import *
import threading
import time
import tkinter.scrolledtext as tkscrolled

# Biblioteca para el uso del carro
from WiFiClient import NodeMCU


# Ventana principal
root = Tk ()
root.title ( ' Proyecto II, I Semestre 2019 ' )
root.minsize ( 1000 , 500 )
root.resizable ( width = NO , height = NO )



# text boxes and their names
Title1 = Label (root, text = "Messages sent", font = ('Arial', 14), fg = 'black')
Title1.place (x = 190, y = 65)

Title2 = Label (root, text = "Message received", font = ('Arial', 14), fg = 'black')
Title2.place (x = 650, y = 65)

send = tkscrolled.ScrolledText (root, height = 14, width = 45)
send.place (x = 90, y = 105)

Receive = tkscrolled.ScrolledText (root, width = 45, height = 15)
Receive.place (x = 530, y = 105)

# The client is created for NodeMCU
carro = NodeMCU ()
carro.start ()

def get_messages ():
    index = 0
    while (carro.loop):
        while (index <len (carro.log)):
            msg_envio = "[{0}] cmd: {1} \ n" .format (index, carro.log [index] [0])
            send.insert (END, msg_envio)
            send.see ("end")

            msg_recibido = "[{0}] result: {1} \ n" .format (index, carro.log [index] [1])
            receive.insert (END, msg_recibido)
            receive.see ('end')

            index += 1
        time.sleep (0.200)

def send (event):
   
    message = str (command.get ())
    if (len (message)> 0 and message [- 1] == ";"):
        command.delete (0, 'end')
        carro.send (message)
    else:
        messagebox.showwarning ("Error in the message", "Message without completion character ';'")


# The enter key is linked to the send function
root.bind ('<Return>', send)

p = threading.Thread(target = get_messages)
p.start ()
           

title = Label (root, text = "Message:", font = ('Agency FB', 14), fg = 'black')
title.place (x = 100, y = 360)

command = Input (root, width = 30, font = ('Agencia FB', 14))
command.place (x = 200, y = 360)




# Buttons

Btn_1 = Button (root, text = 'Send', command = lambda: send (None), bg = 'blue', font = ('Agencia FB', 12))
Btn_1.place (x = 550, y = 360)


root.mainloop ()

