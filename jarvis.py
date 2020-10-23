import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hrs = int(datetime.datetime.now().hour)
    if hrs >= 0 and hrs < 12:
        speak("Good Morning")
    elif hrs >= 12 and hrs < 18:
        speak("good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir, Please tell me How may i help you")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say it again please: ")
        return("None")
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('your gmail id','your password')
    server.sendmail('your gmail id',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()

    speak("Deepa gadhi hai ")
  
    while(True):
        query = takeCommand().lower()
        # Logic for executing tasks based in query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wekipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        

        elif 'playmusic' in query:
            music_dir ='D:\\My Music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is {strTime}")
        elif 'open code ' in query:
            codepath="C:\\Users\\maazm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to harry' in query:
            try:
                speak("What should i say? ")
                content=takeCommand()
                to="dhakadneeraj786@gamil.com "
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend neeraj i am not able to send the email")