#*-* coding : utf-8 *-*
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
import pyttsx
from datetime import datetime
import webbrowser

def RecordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Birseyler Soyle!")
        audio = r.listen(source)
     
    data = ""
    try:
        data = r.recognize_google(audio)
        print("Soyledigin: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Sesini algilayamadi")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def jarvis(data):
    if "time" in data:
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[42].id)
        engine.say(datetime.now().strftime('%d-%m-%Y'))
        engine.runAndWait()

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        webbrowser.open_new("https://www.google.com/maps/place/" + location + "/&amp;")


data = RecordAudio()
jarvis(data)

while 1:
    data = RecordAudio()
    jarvis(data)
