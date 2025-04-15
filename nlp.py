import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "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"

r = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('voice', 'en-in')
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

conversation = list()
conversation.append("The following is a conversation with an AI. This AI is helpful, creative, clever and very friendly. AI's name is Olia.")

speak("hello vrashni, how can i help you")

