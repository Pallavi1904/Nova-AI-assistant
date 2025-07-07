     # NOVA – Symbolizing innovation and intelligence.

import speech_recognition as sr
import webbrowser  # built in library
import pyttsx3 
import musicLibrary
import requests 
# from gtts import gTTS
from openai import OpenAI 
# import pygame
import os

engine = pyttsx3.init()

def openai(command):
    client = OpenAI(
    api_key="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")

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"system", "content":"you are a virtual assistant named Nova skilled in general task like alexa and google cloud"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content  

def speak(text):
    engine.say(text)
    engine.runAndWait()




def ProcessesCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        output = openai(c)
        speak(output)
        print(output)


if __name__ == "__main__":
    speak("Initializing Nova......")
    r = sr.Recognizer() 
    # Listen for word Nova  to wake up
    # Obtain audio from microphone
    while True:
            print("Recognizing.....")
            # Recognising speech using google
            try:
                with sr.Microphone() as source:
                    # r.adjust_for_ambient_noise(source, duration=2)
                    print("Say 'Nova' to activate me.")
                    print("Listening....!")
                    audio = r.listen(source, timeout=4, phrase_time_limit=4) #timeout = wait for that much sec to speech phrase =Once the user starts speaking, it records only for given 1 seconds, then stops.
                    word = r.recognize_google(audio)
                    print(f"Recognized: {word}")
                    if(word.lower() == "nova"):
                        speak("yea, how can i assist you?")
                        with sr.Microphone() as source:
                            print("Nova active...!")
                            audio = r.listen(source)
                            command = r.recognize_google(audio)
                            print(f"Command Recognized: {command}")
                            ProcessesCommand(command)

            # except Exception as e:
            #     print("Error: {0}".format(e))
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase. Try speaking louder or check the mic.")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                print("Exiting Nova... Goodbye!")
                speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
