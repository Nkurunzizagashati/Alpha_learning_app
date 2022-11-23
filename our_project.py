import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

outcomes = "Welcome to the world of searching knowledge and skills. At the end of the program you should be able to write and spell the alphabet, connect multiple alphabets to make a spelled word, write the names of things that surround you, and communicate through writing. You should also have the basic skills to perform well the rest of your education journey. Now, it is time to start the program, welcome!"
guidelines = "Hello! thank you for your interest in learning alphabet and you're welcome on Alpha_learning_app. This is a game that will help you to learn the aphabet. The game has 3 levels: level 1 for beginners, level 2 for intermediate, and level 3 which is the advanced level. At the end of each level you will be given a quiz which you must pass with at least 75% to continue to the next level. If you fail the quiz, you will have a chance to repeat again. Good luck"
alphabet = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"

def out_come(outcomes):
    speak(outcomes)


def guide_line(guidelines):
    speak(guidelines)
     

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("SAY SOMETHING...")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        return text
    except:
        print("Sorry could not recognize what you said")


def speak(text):              # our function that takes in text as a parameter
    tts = gTTS(text=text, lang="en")    #this function converts the entered text to speech, in the language selected
    filename = "voice.mp3"      # creating an empty mp3 file and assigning it to the variable filename
    tts.save(filename)            #saving our speech to the mp3 file
    playsound.playsound(filename)   #playing our speech
    os.remove(filename)

def option():
    user_option = input("WOULD YOU LIKE TO CONTINUE? y/n ")
    if user_option.upper() == "Y":
        pass
    elif user_option.upper() == "N":
        print("quitting....")
        quit()
    else:
        print("INVALID INPUT")    


out_come(outcomes)
guide_line(guidelines)
speak(alphabet)


    