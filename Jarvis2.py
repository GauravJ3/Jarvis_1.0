import pyttsx3
import datetime

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



if __name__ == "__main__":
    greet()