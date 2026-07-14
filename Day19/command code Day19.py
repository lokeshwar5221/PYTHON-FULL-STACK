import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

engine=pyttsx3.init()

def speak(Text):
    engine.say(Text)
    engine.runAndWait()

def take_command():
    recognizer=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listining")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    try:
        print("recognizing....")
        command=recognizer.recognize_google(audio)
        print("You said:",command)
        return command.lower()
    except Exception:
        print("sorry,please say that again")
        return None


def with_user():
    hour=datetime.datetime.now().hour
    if hour<12:
        speak("good morning \nI am your virtual assistant")
    if hour<18:
        speak("good afternoon \nI am your virtual assistant")
    else:
        speak("good evening \nI am your virtual assistant")
with_user()

while True:
    command=take_command()
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
    elif "open youtube"in command:
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        webbrowser.open("https://www.google.com/")
    #elif "open spotify" in command:
     #   os.startfile('"C:\Users\lokes\OneDrive\Documents\Desktop\Spotify.lnk')

    elif "who is" in command:
        person=command.replace("who is","")
        info=wikipedia.summary(*args,command,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("goodbye")
        break
