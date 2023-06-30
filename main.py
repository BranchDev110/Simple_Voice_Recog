import os
import time
import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    print (sr.Microphone.list_microphone_names())
    with sr.Microphone(device_index=6) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()

print (text)