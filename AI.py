from gtts import gTTS
import os
import speech_recognition as sr
import openai
import time
import sys
import pyttsx3
import vlc
from configparser import ConfigParser

config = ConfigParser()
config.read('LuminaConfig.conf')

config.readfp(open(r'LuminaConfig.conf'))
openai.api_key = config.get('LuminaMatrixConfig', 'APIkey')
ASSISTANT_ID = "asst_Cz529hvrKSIUBryFJBR6F2Xf"


def luminaAi(prompt):
    thread = openai.beta.threads.create(messages=[{"role": "user", "content": prompt,}])
    run = openai.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    
    while run.status != "completed":
        print("A Carregar...")
        run = openai.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        aguarde = vlc.MediaPlayer('/home/pires/Desktop/build/lumina_waiting.mp3')
        aguarde.play()
        
        time.sleep(1)
        aguarde.stop()
        
        
    
    if run.status == "completed":
        messages = openai.beta.threads.messages.list(
            thread_id= thread.id
        )
       
        for msg in messages.data:
            role = msg.role
            content = msg.content[0].text.value
            print(content)
            falar(content)
            os.execv(sys.argv[0], sys.argv)

   




def falar(text):
    tts = gTTS(text=text, lang='pt', tld='pt')
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")

def reconhecer():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pode Falar.")
        audio = recognizer.listen(source,timeout=0)  

    try:
        dados = recognizer.recognize_google(audio, language="pt-pt")
        luminaAi(dados) 
    except sr.UnknownValueError:
        print("Ocorreu um erro ao reconhecer o áudio!")
        falar("Ocorreu um erro ao reconhecer o áudio! Exprimente tentar novamente mais tarde!")
    except sr.RequestError as e:
        print("Erro ao solicitar resultados:", e)
    except TimeoutError:
        falar("Ocorreu um erro ao reconhecer o áudio! Exprimente tentar novamente mais tarde!")
        




def ativar():
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        
            try:
                trigger = recognizer.recognize_google(audio, language="pt-PT")
                print("OK", trigger)
                
                if 'lumina' in trigger.lower() or 'Lumina' in trigger.lower() :

                    falar("Sim?")
                    reconhecer()
            except Exception as e:
                print("Erro:", e)

if __name__ == '__main__':
    ativar()
