import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import datetime
import wikipedia
import webbrowser
import requests
import pyjokes
import time
import shutil
import subprocess
import screen_brightness_control

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.reco(audio, language='en')
        print(f"You said: {query}")
    except:
        print("Sorry, I didn't hear that. Please say that again.")
        return ""
    return query.lower()

def greet():
    speak('Activating S H I P Dektop assistant.')
def ai_tasks():

    while True:
        command = takeCommand()

        if 'what is' in command:
            search_query = command.replace('what is', '')
            wikipedia_summary = wikipedia.summary(search_query, sentences=1)
            print(wikipedia_summary)
            speak(wikipedia_summary)

        elif 'play' in command:
            song = command.replace('play', ' ')
            speak('Playing')
            speak(song)
            print('Playing: ', song)
            pywhatkit.playonyt(song)

        elif 'what time is it' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The current time is {current_time}")
            speak(f"The current time is {current_time}")


        elif 'where is ' in command :
            command = command.replace("where is ","")
            location = command
            url = 'https://www.google.com/maps/place/' + location
            webbrowser.open(url)

        elif 'locate' in command:
            command = command.replace("locate ", "")
            location = command
            url = 'https://www.google.com/maps/place/' + location
            webbrowser.open(url)


        elif 'power point' in command:
            speak("opening Power Point presentation")
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(power)
        elif 'who are you' in command:
            speak('I am shhip')
        elif 'excel' in command or 'microsoft excel' in command:
            speak("opening Microsoft Excel")
            excel = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(excel)

        elif 'onenote' in command:
            speak("opening onenote")
            note = r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE"
            os.startfile(note)

        elif "hibernate" in command or "sleep" in command:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in command or "sign out" in command:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'word' in command or 'microsoft word' in command:
            speak("opening Microsoft word")
            word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(word)

        elif 'open lms' in command:
            webbrowser.open_new('https://lms.cuchd.in/login/index.php')

        elif 'open cuims' in command:
            webbrowser.open_new('uims.cuchd.in/uims/')

        elif 'open google' in command or 'open chrome' in command:
            webbrowser.open_new('google.com')

        elif 'ship' in command :
            speak('Yes sir, how can I help you ')

        elif 'brightness' in command:
            # t = int(input("Please input what percentage of brightness you want: "))
            screen_brightness_control.set_brightness(10)
        elif 'send message' in command and 'whatsapp' in command:
            mess = takeCommand()
            mobile = input('Enter mobile number: ')
            speak('Please login to whatsapp account.')
            pywhatkit.sendwhatmsg(mess, mobile, datetime.datetime.hour, datetime.datetime.minute)
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")

        elif 'stop' in command.lower() or 'exit' in command.lower() or 'quit' in command.lower():
            print("Goodbye!")
            speak("Goodbye!")
            exit()

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        elif "weather" in command:
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(
                    weather_description))

            else:
                speak(" City Not Found ")

        elif 'search' in command or 'look for ' in command:
            command = command.replace("search", "")
            webbrowser.open(command)

        elif "who i am" in command:
            speak("If you talk then definitely you are a human.")

        elif 'username' in command or 'set user ' in command:
            speak('What should i call you sir')
            u_name = takeCommand()
            speak('Welcome mister ', u_name)
            columns = shutil.get_terminal_size().columns
            print("Welcome ", u_name)
            speak('How can I help you, sir')
        elif 'open youtube' in command:
            webbrowser.open_new('Youtube.com')
        elif "" in command:
            continue
        else:
            speak("Sorry, I don't know how to do that yet.")
