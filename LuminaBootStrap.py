


## Lumina BootStrap  -- 2024 PiresWorks

###################################################################################
#  Este Pequeno programa testa e confirma a presença  do arduino pela Porta COM.  #
#  Sendo ela  neste caso a porta COM: "/dev/ttyACM0".                             #
#  Arrancando por fim, O Programa com as condições detetadas.                     #
###################################################################################

import serial
import os
from tkinter import *
from pynput.keyboard import Key, Listener
from PIL import ImageTk
import PIL.Image

from MAIN import *


import keyboard
import threading



splash_root = Tk()

splash_root.geometry("500x200")
splash_root.wm_attributes('-type','splash')
splash_root.configure(background='black')

frame = Frame(splash_root, width=500, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)




img = ImageTk.PhotoImage(PIL.Image.open("LOGO.png"))
label = Label(frame, image = img)

label.pack()

def Boot():
    try:
        arduino = serial.Serial('/dev/ttyACM0')  #TESTE PORTA COM. LIGADO OU NAO AO MATRIX (ARDUINO)
        if arduino.is_open:
                print("DEBUG: PORTA COM FUNCIONAL!")
                EstadoCOM = "Conectado na porta COM: /dev/ttyUSB0"
                Vermelho = True
                LuminaBegin(Vermelho,EstadoCOM)
        
    except serial.SerialException as e:
            print(" ")
            print(" ")
            print("DEBUG: PORTA COM  OFF")
            EstadoCOM = "\n \n \n Erro: Matrix (Arduino) não Conectado.\n Certifique-se que o USB está ligado \n e que a porta COM não está obstruida."
            Vermelho = False
            splash_root.destroy()
            LuminaBegin(Vermelho,EstadoCOM)
      


def LuminaSelfPINGCheck():
    
    hostname = "google.com" 
    resposta = os.system(f"ping -c 1  {hostname}")
    
    if resposta == 0:   #PING OK
         Boot()
    else:  #PING OFF
         print(" ")
         print(" ")
         print("Lumina: Erro 3: OpenAI  OFFLINE")
         
         def fechar():
              erro.destroy()
              splash_root.destroy()
         def TentarN():
              python = sys.executable
              os.execl(python, python, * sys.argv)
         erro= Tk()

         erro.geometry("500x100")
         erro.title("LuminaMatrix")

         canvas= Canvas(erro, width= 500, height= 100, bg="#242424")

         canvas.create_text(250, 25, text="Lumina não conseguiu Estabelecer Ligação a OpenAI (Codigo Erro 3)", fill="white", font=('Helvetica 11'))
         canvas.pack()
         
         ok = Button(erro, text="OK",command=fechar)
         ok.place(x=150,y=50)
         tentar = Button(erro, text="Tentar Novamente",command=TentarN)
         tentar.place(x=225,y=50)
         erro.mainloop()

splash_root.after(3000, LuminaSelfPINGCheck)
splash_root.mainloop()


