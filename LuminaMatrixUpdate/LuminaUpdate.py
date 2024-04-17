
import git
import shutil
import os
import filecmp
from difflib import Differ
import time
## Lumina Update  -- 2024 PiresWorks

###################################################################################
#  Este programa confirma a existencia de uma atualização comparando              #
#  Um ficheiro txt com a build number. se for diferente, existe uma atualização   #
###################################################################################


def CheckUpdate():
    luminaGIT = git.cmd.Git()

    if os.path.isdir("LuminaMatrixUpdateBN") == True:
        shutil. rmtree('LuminaMatrixUpdateBN')
        luminaGIT.clone("https://github.com/PiresFrancisco/LuminaMatrixUpdateBN")
    else:
        luminaGIT.clone("https://github.com/PiresFrancisco/LuminaMatrixUpdateBN")

    time.sleep(1)

    blocal = open("LuminaBuildNumber.txt",'r')
    bserver = open("./LuminaMatrixUpdateBN/LuminaBuildNumber.txt",'r')

    blocal_dados = blocal.readlines()
    bserver_dados = bserver.readlines() 
  
    for i in range(len(blocal_dados)):
        if blocal_dados[i] == bserver_dados[i]:
            print("DEBUG: Não existem atualizações disponiveis")
            


        elif blocal_dados[i] != bserver_dados[i]:
            print("\n \n")
            print("\n \n")
            print("DEBUG: existem atualizações disponiveis")
            time.sleep(3)
            print("\n \n")
            print("A COMEÇAR PROCESSO DE ATUALIZAÇÂO!")
            time.sleep(3)
            print("\n \n")
            print("LuminaMatrix está a encerrar...")
            time.sleep(2)

            



CheckUpdate()

