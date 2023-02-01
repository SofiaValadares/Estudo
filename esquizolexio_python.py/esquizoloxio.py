import speech_recognition as sr
import pyttsx3
import definir_nome
import semana

nome_paciente = None
nome_assistente = None

try:
    definir_nome()
except:
    print('Erro')

semana()

