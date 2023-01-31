import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()

maquina = pyttsx3.init()
maquina.say('Ola mundo, meu nome e Mauricio')
maquina.runAndWait()

try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'maurício' in comando:
            print('Ola Sofia!')
            maquina.say(comando)
            maquina.runAndWait()

except:
    print('Microfone ruim')