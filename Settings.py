
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *

from configparser import ConfigParser

import os
import webbrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pires/PAP FIGMA/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def LuminaDefs(event):
    defs = Tk()
    
    defs.geometry("512x496")
    defs.configure(bg = "#FFFFFF")
    defs.title("LuminaMatrix Settings")

    def SairGuardar():
        print("DEBUG: INICIAR FUNÇ GUARDAR")

        def ProcessoGuardar():
            config = ConfigParser()
            config.read('LuminaConfig.conf')
            config.set('LuminaMatrixConfig', 'SliderVolume', '0')
            config.set('LuminaMatrixConfig', 'MatrixBaudRateArduino', '9600')
            config.set('LuminaMatrixConfig', 'LuminaMute', 'true')
            config.set('LuminaMatrixConfig', 'RateFalaVelocidade', '50')

            
            temperaturaLumina = temperatura.get()
            print(temperaturaLumina)
            config.set('LuminaMatrixConfig', 'temperaturalumina', str(temperaturaLumina))



            with open('LuminaConfig.conf', 'w') as f:
                config.write(f)



        ProcessoGuardar()
        defs.destroy()

    canvas = Canvas(
            defs,
            bg = "#FFFFFF",
            height = 512,
            width = 512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
    
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
            0.0,
            0.0,
            512.0,
            512.0,
            fill="#242323",
            outline="")


    temperatura = Scale(defs, from_=0, to=7, orient=HORIZONTAL,bg="#242323",bd=0,fg='white',length='450')
    temperatura.set(7)
    temperatura.pack(padx=25, pady=150,anchor=NW)


    bsair = Button(canvas, text="Guardar",command=SairGuardar)
    bsair.config(
        bd=0,
        foreground="white", 
        background="#242323",
    )
    bsair.place(x=225,y=450)

    canvas.create_text(
            18.0,
            16.0,
            anchor="nw",
            text="Definições",
            fill="#FFFFFF",
            font=("Product Sans", 48 * -1),
            tags="TextoCima"
        )
    
    canvas.create_text(
            19.0,
            110.0,
            anchor="nw",
            text="Escala de Temperatura da Lumina:",
            fill="#FFFFFF",
            font=("Product Sans", 25 * -1),
            tags="tempAI"
        )
    
    ajudaTEMPAI = canvas.create_text(
            410.0,
            120.0,
            anchor="nw",
            text="O que é isto?",
            fill="lightblue",
            font=("Product Sans", 11 * -1),
            tags="ajudaTEMPAI"
        )


    def HLajudaTEMP(event):
        webbrowser.open_new("https://google.com")


    canvas.tag_bind(ajudaTEMPAI,'<Button-1>',HLajudaTEMP)

    defs.resizable(False, False)
    defs.mainloop()
