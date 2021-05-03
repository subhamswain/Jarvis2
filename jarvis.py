import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import pyautogui
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am RACHAEL sir.Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    #r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print("user said"+ query)

    except Exception as e:
        print(e)
        print("say that again please..")
        return None

    return query



#if __name__=="__main__":
    #wishMe()
def main():
  while True:
    query=takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia..')
        s=query.replace("wikipedia"," ")
        result=wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
            #print(results)
        speak(result)

    elif 'open youtube' in query:
        speak("About what you want to search on Youtube")
        s=takeCommand()
        webbrowser.open("https://www.youtube.com/results?search_query="+s+"")

    elif 'minimise the windows' in query:
        pyautogui.hotkey('Win','d')

    elif 'new tab' in query:
        pyautogui.hotkey('ctrl','t')

    elif 'volume up' in query:
        pyautogui.hotkey('volumeup') 

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'stackoverflow' in query:
        webbrowser.open("stackoverflow.com") 

    elif 'play music' in query:
        music_dir = 'H:\\songs' 
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[2]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strTime}")

if __name__=="__main__":
    wishMe()
    main()