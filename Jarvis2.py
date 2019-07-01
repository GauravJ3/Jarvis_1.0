import pyttsx3
import datetime
import speech_recognition as sr    #Library for performing speech recognition with the Google Speech Recognition API
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def say(audio):
    engine.say(audio)
    engine.runAndWait()   # Blocks while running all the queued commands
    
def greet():
    '''
        This will greet me..
    '''
    # Get the current hr
    hr = datetime.datetime.now().hour
    if hr >= 6 and hr < 12:
        say("Good Morning Master Gaurav")
    elif hr >= 12 and hr < 16:
        say("Good evening Master Gaurav")
    elif hr == 23:
        say("It's time to shut down the laptop and have a good night sleep master")
        say("Shutting everything down...")
        quit()
    say("Hi.. My name is Alfred, I'm your personal assistant, how may i help you?")

def takeCommand():
    r = sr.Recognizer()                                     # Make a recogizer for microphone
    with sr.Microphone() as source:                         # Capturing voice
        print("Listening ....")
        r.pause_threshold = 1.0                            # By default pause_threshold is 0.5
        r.adjust_for_ambient_noise(source, duration = 1.0)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = r.listen(source)                            # now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")     # recognizing the voice, converting speech to text
            print(f"User said: {query}")
        except Exception as e:
            print(e)                                        # Printing the error
            return "None"
        return query


if __name__ == "__main__":
    greet()
    user_query = takeCommand().lower()
    if "youtube" in user_query:
        webbrowser.get().open("https://youtube.com/")
    if "stackoverflow" in user_query:
        webbrowser.get().open("https://www.stackoverflow.com/")