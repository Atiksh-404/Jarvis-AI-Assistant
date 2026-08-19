import speech_recognition as sr
import webbrowser
import pyttsx3
from modules.ai import ask_ai
import pygame
from modules.time_utils import get_time
from modules.weather import get_weather
from modules.news import get_news
from modules.youtube import play_on_youtube

r = sr.Recognizer()

r.energy_threshold = 250
r.dynamic_energy_threshold = True
r.pause_threshold = 1.2

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print("Available voices:")

for i, voice in enumerate(voices):
    print(i, voice.name)

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

def play_yes_boss():
    pygame.mixer.music.load("assets/yesboss.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

async def speak_async(text):
    filename = "voice.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-GuyNeural"
    )

    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)

def speak(text):
    asyncio.run(speak_async(text))

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        answer = "Opening Google."
        speak(answer)
        return answer
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        answer = "Opening Youtube."
        speak(answer)
        return answer
    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        answer = "Opening Linkedin."
        speak(answer)
        return answer
    
    elif "open outlook" in c.lower():
        webbrowser.open("https://outlook.com")
        answer = "Opening Outlook."
        speak(answer)
        return answer
    
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        title = play_on_youtube(song)
        if title:
            answer = f"Playing {title}"
        else:
            answer = "Sorry Boss. I couldn't find that song."
        speak(answer)
        return answer
        
    elif  "time" in c:
        answer = get_time()
        print(answer)
        speak(answer)
        return answer

    elif "weather" in c:
        city = "Noida"

        if "in" in c:
            city = c.split("in",1)[1].strip()
        answer = get_weather(city)
        print(answer)
        speak(answer)
        return answer
        
    elif "news" in c:
        topic = "India"

        if "ai" in c:
            topic = "Artificial Intelligence"

        elif "sports" in c:
            topic = "Sports"

        elif "technology" in c or "tech" in c:
            topic = "Technology"

        elif "business" in c:
            topic = "Business"

        elif "world" in c:
            topic = "World"

        headlines = get_news(topic)

        text = f"Here are the latest {topic} headlines.\n\n"

        for headline in headlines:
            text += headline + "\n"

        speak(f"Here are the latest {topic} headlines.")

        for headline in headlines:
            speak(headline)

        return text
    
    
    else:
        # Let AI handel the request

        answer = ask_ai(c)

        print("=" * 50)
        print("answer =", repr(answer))
        print("type =", type(answer))
        print("=" * 50)

        speak(str(answer))
        return answer
    
            
def listen_for_command():
    with sr.Microphone() as source:

        print("Listening...")

        r.adjust_for_ambient_noise(source, duration=0.5)

        audio = r.listen(
            source,
            timeout=5,
            phrase_time_limit=15
        )

    command = r.recognize_google(
        audio,
        language="en-IN"
    ).strip().lower()

    return command

def wait_for_wake_word():

    while True:

        try:
            word = listen_for_command()

            if not word:
                continue

            print("Heard:", word)

            if "jarvis" in word:

                play_yes_boss()

                return True

        except Exception as e:
            print(e)

def listen_after_wake():

    try:

        print("Waiting for command...")

        command = listen_for_command()

        return command

    except Exception:

        return None
    

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen to the wake word "Jarvis"
        # Obtain audio from the microphone

        print("recognizing.....")
        # Recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            text = r.recognize_google(audio, language="en-IN").lower().strip()
            print("Heard:", text)
            if "jarvis" in text:
                command = text.replace("jarvis", "").strip()
                if command == "":
                    play_yes_boss()
                # Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Active....")
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source, timeout=5, phrase_time_limit=15)
                    command = r.recognize_google(audio, language="en-IN").strip().lower()
                    print("Command:", command)

                    processCommand(command)
                else:
                    processCommand(command)
                 
        except Exception as e:
            print("Error {0}".format(e))

