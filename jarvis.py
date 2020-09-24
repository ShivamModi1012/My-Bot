import datetime
import wikipedia
import pyttsx3
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    speak("I am Jarvis Sir. Please tell me, how may I help you?")

def takeCommand():
    # it take microphone input from user and return audio output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please!!")
        return "None"
    return query

#def sendEmail(to,content):


if __name__=="__main__":
   wishMe()
   while True:
        query = takeCommand().lower()

        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is{strTime}")

       # elif 'email' in query:
        #    try:
         #       speak("What to send")
          #      content = takeCommand()
           #     to = "shivammodi1012@gmail.com"
            #    sendEmail(to, content)
             #   speak("Email sent!")
            #except Exception as e:
             #   print(e)
              #  speak("Sorry, I am not able to sent email")
        elif "quit" in query:
            speak("Thank you sir for your time!!")
            quit()
