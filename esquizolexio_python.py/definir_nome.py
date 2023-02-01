import speech_recognition as sr
import pyttsx3

def nome(audio):
    try:
        with sr.Microphone() as source:
            print('Ouvindo...\n')
            voz = audio.listen(source)
            nome = audio.recognize_google(voz, language='pt-BR')
            return nome
    
    except:
        print('Erro: Microfone ruim.')

def falar(frase, maquina):
    print(frase)
    maquina.say(frase)
    maquina.runAndWait()
        

audio = sr.Recognizer()
maquina = pyttsx3.init()

frase = 'Ola, eu sou um assistente virtual que ira conduzir sua consulta. Qual é seu nome?'
falar(frase, maquina)

nome_paciente = nome(audio)

frase = f'Prazer {nome_paciente} meu nome é... Bem eu não tenho um nome, como você gostaria de me chamar?'
falar(frase, maquina)

nome_assistente = nome(audio)

frase = f'{nome_assistente}... Gostei do nome'
falar(frase, maquina)
