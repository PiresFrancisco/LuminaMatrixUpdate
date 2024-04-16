


#2024 PiresWorks //PROJETO PAP - App LuminaMatrix
# UI/UX Feito no Figma 

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import sys
import os

from TkVisualizer import TkAudioVisualizer

from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8

from Settings import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/pires/PAP FIGMA/build/assets/frame0")

from AI import *

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def LuminaBegin(Vermelho,EstadoCOM):

    def AIbegin(event):
        print("Debug:Ready!")
        print("Lumina Begin")
        reconhecer()
    
    
    
    def desativado(event):
        print("NAO DISPONIVEL")
        python = sys.executable
        os.execl(python, python, * sys.argv)

   

    main = Tk()

    main.geometry("512x512")
    main.configure(bg = "#FFFFFF")
    
   
    main.title("LuminaMatrix")

    canvas = Canvas(
        main,
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

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        256.0,
        48.0,
        image=image_image_1
    )


    canvas.create_text(
        250.0,
        45.0,
        anchor="center",
        text="LuminaMatrix",
        fill="#FFFFFF",
        font=("Inter", 36 * -1)
    )

    if Vermelho == True:
        canvas.create_text(
        250.0,
        381.0,
        anchor="center",
        text=EstadoCOM,
        fill="#FF0000",
        font=("Inter", 14 * -1)
    )
        canvas.create_text(
        250.0,
        351.0,
        anchor="center",
        text="Não Disponível",
        fill="#FF0000",
        font=("Inter", 14 * -1)

    )
        
        image_image_6 = PhotoImage(
        file=relative_to_assets("off.png"))
        image_6 = canvas.create_image(
        256.0,
        232.0,
        image=image_image_6,
    )
        canvas.tag_bind(image_6,'<Button-1>',desativado)

    if Vermelho == False:
        
        canvas.create_text(
        250.0,
        381.0,
        anchor="center",
        text=EstadoCOM,
        fill="#008000",
        font=("Inter", 14 * -1)
        ) 
        
        canvas.create_text(
        250.0,
        351.0,
        anchor="center",
        text="A Espera da KeyWord 'Lumina'",
        fill="#FFFFFF",
        font=("Inter", 14 * -1)

    )
        image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image (
        256.0,
        232.0,
        image=image_image_6,
        
    )
    
    def Reset():
        main.update_idletasks()


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        443.0,
        228.0,
        image=image_image_2
    )


    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        443.5491943359375,
        228.67681884765625,
        image=image_image_3
    )
    
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        69.0,
        228.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        69.16665649414062,
        229.16668701171875,
        image=image_image_5
    )
    canvas.tag_bind(image_4,'<Button-1>',LuminaDefs)
    canvas.tag_bind(image_5,'<Button-1>',LuminaDefs)

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        256.0,
        237.0,
        image=image_image_7
    )

    


    if Vermelho == True:
        canvas.tag_bind(image_7,'<Button-1>',desativado)
    else:
        canvas.tag_bind(image_7,'<Button-1>',AIbegin)


    
    
    
    main.resizable(False, False)
    main.mainloop()





