
import speech_recognition as sr
from say import say


def takeCommand():
    r = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source, 8, 10)
        try:
            print("recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            say("Please try again sir..")
            return "Some error occured Sorry sir..."
