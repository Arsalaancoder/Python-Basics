import pyttsx3
import speech_recognition as sr
import datetime

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("good morning Arsalaan !")

    elif hour>=12 and hour<18:
       speak("good Afternoon Arsalaan !")
    else:
      speak("good evening Arsalaan")
      speak("how are you")
      speak("the manger has send an email for the project")
def greet():
  speak("sleep at 8:00 PM")




if __name__== "__main__":

    wishme()
    greet()

