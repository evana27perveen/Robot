from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from translate import Translator
from gtts import gTTS
import os
import speech_recognition as sr

chatbot = ChatBot('Shoshi')
rec = sr.Recognizer()
trans = Translator(to_lang='bn')

def getting_data_from_user():
    with sr.Microphone() as source:
        audio = rec.listen(source, 100)
        try:
            text = rec.recognize_google(audio)
            r = str("".format(text))
        except:
            getting_data_from_user()
    return r

trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train("chatterbot.corpus.english")

while True:
    print("You: ")
    r = getting_data_from_user()
    res = chatbot.get_response(r)
    print("Robot: ",res)
    print(type(res))
    pic = str(res)
    print(type(pic))
    translation = trans.translate(pic)
    tts = gTTS(text=translation, lang='bn')
    tts.save("Test.mp3")
    os.system("mpg321 Test.mp3")