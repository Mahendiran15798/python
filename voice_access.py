import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
        hour=int(datetime.datetime.now().hour)

        if hour>=0 and hour<12:
            speak("   good morning")
        elif hour>=12 and hour<= 19:
            speak("   Good afternoon")
        else:
            speak("  Good evening")
speak(" hey im there......, what can i do")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print(" Wait for a moment's . . .")
        query=r.recognize_google(audio,language ='en-in')
        print("  ",query)
    except Exception as e:

        speak("ok, how can i help you mahi")
        if e in query:
            speak(" how can i help you")
        speak("closing....")
    return query

if __name__ == '__main__':
        wishme()
        while True:
            query=takecommand().lower()
            if "wikipedia" in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", " ")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("According to wikipedia")
                speak(results)
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open google chrome" in query:
                webbrowser.open("google chrome.com")
            elif " shutdown " in query:
                os.system("shudown /l")
                speak("1. Shutdown Computer");
                speak("2. Restart Computer");
                speak("3. Exit");
                choice = int(input("\nEnter your choice: "));
                if (choice >= 1 and choice <= 2):
                    if choice == 1:
                        os.system("shutdown /l /t 0");
                    else:
                        os.system("shutdown /l /t 0");
                else:
                    exit();
            elif "ok bye" in query:
                speak("ok bye...., mahi chellam love you....")
                exit()