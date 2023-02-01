import speech_recognition as sr
import pyttsx3

def ouvir(audio):
    try:
        with sr.Microphone() as source:
            print('Ouvindo...\n')
            voz = audio.listen(source)
            discurso = audio.recognize_google(voz, language='pt-BR')
            return discurso
    
    except:
        print('Erro: Microfone ruim.')

def falar(frase, maquina):
    print(frase)
    maquina.say(frase)
    maquina.runAndWait()

audio = sr.Recognizer()
maquina = pyttsx3.init()

palavras = ['culpado', 'culpada', 'não gostam de mim', 'sou direto', 'sou direta']

frase = 'Me fale um pouco sobre sua segunda-feira.'
falar(frase, maquina)

discurso = ouvir(audio)
count = 0

for i in range(len(palavras)):
    palavra = palavras[i]

    if palavra in discurso:
        frase = 'Isso acontece com frequencia?'
        falar(frase, maquina)
        resposta = ouvir(audio)
        resposta = resposta.lower()

        if resposta == 'sim':
            count += 1