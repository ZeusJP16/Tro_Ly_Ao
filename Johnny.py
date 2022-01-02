import pyaudio
import speech_recognition
import pyttsx3
from datetime import date, datetime
import webbrowser
import json
import requests
import subprocess
import wikipedia
import time

Johnny_ear = speech_recognition.Recognizer() #recognizer : nhan dang
Johnny_mouth = pyttsx3.init()
Johnny_brain = ""


def speak(Johnny_brain):
    Johnny_mouth.say(Johnny_brain)
    Johnny_mouth.runAndWait()

def takeCommand():
    Johnny_ear
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio=Johnny_ear.listen(source)

        try:
            Me=Johnny_ear.recognize_google(audio,language='en-US')
        except:
            Me = ""
        return Me

def wishMe():
    hour=datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

wishMe()

if __name__=='__main__':

    while True:
        speak("Can I help you?")
        Me = takeCommand().lower()
        print("Me: " + Me)
        if Me==0:
            continue

        if Me == "":
            Johnny_brain = "I don't understand what you said, try again"

        elif "Hello Johnny" in Me:
            Johnny_brain = "I'm listening"

        elif "today" in Me:
            today = date.today()
            Johnny_brain = "Today is " + today.strftime("%B %d, %Y")
            speak(Johnny_brain)
            print("Johnny: " + Johnny_brain)

        elif "time" in Me:
            now = datetime.now().strftime("%H:%M:%S")
            Johnny_brain = "Now is " + now
            speak(Johnny_brain)
            print("Johnny: " + Johnny_brain)

        elif "weather" in Me:
            api_key="328a533aee2f6134ed13e660bcb3293d"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Weather for where")
            city_name=takeCommand()
            print("Me: " + city_name)
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print("Johnny: Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))
                speak("Temperature in kelvin unit is " +
                    str(current_temperature) +
                    "\n humidity in percentage is " +
                    str(current_humidiy) +
                    "\n description  " +
                    str(weather_description))

            else:
                speak(" City Not Found ")


        elif 'open google' in Me:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(3)

        elif "open stack overflow" in Me:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")

        elif 'who are you' in Me or 'what can you do' in Me:
            speak("I am Johnny")
                
        elif "thank you" in Me:
            Johnny_brain = "See you again"
            print("Johnny: " + Johnny_brain)
            break

    Johnny_mouth.say(Johnny_brain)
    Johnny_mouth.runAndWait()

time.sleep(4)

    