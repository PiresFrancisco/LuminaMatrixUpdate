from gtts import gTTS

import os
import speech_recognition as sr
import random
import subprocess
import time




def ai_media_pausa():
    subprocess.run(["playerctl", "pause"])
    nomemusica = subprocess.check_output(["playerctl", "--format", "'{{artist}} - {{title}}'", "metadata"], text=True)
    falar("Ok. Canção")
    falar(nomemusica)
    falar("em pausa.")


def ai_qual_musica ():
    subprocess.run(["playerctl", "pause"])
    nomemusica = subprocess.check_output(["playerctl", "--format", "'{{artist}} - {{title}}'", "metadata"], text=True)
    falar(nomemusica)
    subprocess.run(["playerctl", "play"])


def ai_media_anterior():
    falar("Ok. A Tocar canção anterior.")
    subprocess.run(["playerctl", "previous"])
    subprocess.run(["playerctl", "previous"])
    time.sleep(1)
    nomemusica = subprocess.check_output(["playerctl", "--format", "'{{artist}} - {{title}}'", "metadata"], text=True)
    falar(nomemusica)


def falar(text):
    tts = gTTS(text=text, lang='pt')
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")


def ai_media_proxima():
    falar("Ok. Próxima Canção.")
    subprocess.run(["playerctl", "next"])
    time.sleep(1)
    nomemusica = subprocess.check_output(["playerctl", "--format", "'{{artist}} - {{title}}'", "metadata"], text=True)
    falar(nomemusica)


def ai_media_resumir():
    falar("Ok. a Resumir a  Música")
    nomemusica = subprocess.check_output(["playerctl", "--format", "'{{artist}} - {{title}}'", "metadata"], text=True)
    falar(nomemusica)
    subprocess.run(["playerctl", "play"])



def ai_media_parar():
    falar("Ok. Vou Parar a Música")
    subprocess.run(["playerctl", "stop"])