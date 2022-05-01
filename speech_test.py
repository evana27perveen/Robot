import speech_recognition as sr

say = sr.Recognizer()
d = "I don't understand"
def speech_text():
    with sr.Microphone() as source:
        audio = say.listen(source=source, phrase_time_limit=10)
        print("I have taken the sound. \n")
        try:
            return say.recognize_google(audio)
        except:
            return d
