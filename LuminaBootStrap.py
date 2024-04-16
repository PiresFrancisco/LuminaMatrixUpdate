


## Lumina BootStrap  -- 2024 PiresWorks

###################################################################################
#  Este Pequeno programa testa e confirma a presença  do arduino pela Porta COM.  #
#  Sendo ela  neste caso a porta COM: "/dev/ttyACM0".                             #
#  Arrancando por fim, O Programa com as condições detetadas.                     #
###################################################################################

import serial
import os
import tkinter
from pynput.keyboard import Key, Listener

from MAIN import *


import keyboard
import threading


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
            EstadoCOM = "\n \n \n Erro 1: Matrix (Arduino) não Conectado.\n Certifique-se que o USB está ligado \n e que a porta COM não está obstruida."
            Vermelho = False
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

#COMEÇAR TESTE PING
LuminaSelfPINGCheck()
