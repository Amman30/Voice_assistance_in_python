import speech_recognition as sr
import pyttsx3
import pywhatkit
import date time
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


def Welcome():
    engine.say("Hello I am Your Voice Assistance")


def input(incomming):
    engine.say(incomming)
    engine.runAndWait()


def incomingCommand():
    try:
        with sr.Microphone() as source:
            print("listening.........")
            voice = listerner.listen(source)
            command = listener.recognizer_google(voice)
            commad = commad.lower()
            if 'alexa' or 'siri' in commad:
                commad = commad.replace("alexa" or "siri", "")
                print(command)
    except:
        pass
    return commad


def start_Voice_Assistance():
    Welcome()
    command = incomingCommad()
    print(commad)
    if 'play' in commad:
        song = commad.replace("play", " ")
        input("playing"+commad)
        pywhatkit.playonyt(commad)
    elif 'time' in commad:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        input("The Clock is Showing:"+time)
    elif 'info' or 'wikipedia' in commad:
        information = wikipedia.summary(person, 2)
        input(information)
    else:
        input("Say it Again")


while True:
    start_Voice_Assistance()
