from gtts import gTTS
import os
from textblob import TextBlob
import random
from translate import Translator
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import datetime
import speech_test

def time():
      now = datetime.now()
      return now.hour
chatbot = ChatBot("Shoshi")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
def responses(put):
    return chatbot.get_response(put)




random_answer = ["Thank you", "Good", "I may be know this before you saying.", "I'm speechless", "Really! Fantastic"
                 "Oh dear, How cute you are!", "So sweet of you", "No, I don't believe"]
time = time()
s = speech_test.speech_text()
trans = Translator(to_lang='bn')
if time>11 and time<=14:
    tts = gTTS(text="Good noon", lang='en')
elif time>1 and time<=11:
    tts = gTTS(text="Good morning", lang='en')
elif time>14 and time<18:
    tts = gTTS(text="Good afternoon", lang='en')
elif time>=18 and time<=23:
    tts = gTTS(text="Good evening", lang='en')
else:
    tts = gTTS(text="Good night", lang='en')
    s = "Bye"

tts.save("wishing_for_time.mp3")
os.system("mpg321 wishing_for_time.mp3")
while True:
    if s == "I don't understand":
        translation_donot = trans.translate("I don't understand. tell me again")
        tts_no_understand = gTTS(text=translation_donot, lang='bn')
        tts_no_understand.save("Output.mp3")
        os.system("mpg321 Output.mp3")
        s = speech_test.speech_text()
        continue

    elif "Bye" in s or "bye" in s:
        translate_to_bye = trans.translate("Okay Bye, Have a good day")
        ttsless = gTTS(text=translate_to_bye, lang='bn')
        ttsless.save("Output.mp3")
        os.system("mpg321 Output.mp3")
        break

    else:
        analysis = TextBlob(s)
        pol = analysis.sentiment.polarity
        if pol > 0:
            output_text = random_answer[random.randrange(len(random_answer))]
            translation_pos = trans.translate(output_text)
            print(translation_pos)
            ttshigh = gTTS(text=translation_pos, lang='bn')
            ttshigh.save("Output.mp3")
            os.system("mpg321 Output.mp3")
        elif pol < 0:
            translation_neg = trans.translate("Don't say something like this")
            print(translation_neg)
            ttsless = gTTS(text=translation_neg, lang='bn')
            ttsless.save("Output.mp3")
            os.system("mpg321 Output.mp3")
        else:
            response = responses(s)
            output_text = str(response)
            translation = trans.translate(output_text)
            print(translation)
            print(output_text)
            ttsx = gTTS(text=output_text, lang='en')
            ttsx.save("Output.mp3")
            os.system("mpg321 Output.mp3")
    s = speech_test.speech_text()
    #s = input()
    # trans_bn_to_en = Translator(to_lang='en')
    # s = trans_bn_to_en.translate(st)
    # print(s)