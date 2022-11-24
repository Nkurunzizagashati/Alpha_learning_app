import sys
import string
import os
import time
import playsound
import random
import speech_recognition as sr
from gtts import gTTS
from random_word import RandomWords
import getpass

my_dict = {'karenzi': '@12345'}


#asking our user to login
running = True
while running:
    user_response = input("ARE YOU NEW TO THE ALPHA KIDS APP?:  Y/N")
    if user_response.upper() == "Y":
        print("PLZ CREATE AN ACCOUNT")
        user_name = input("PLZ ENTER YOUR NAME: ")
        user_password = getpass.getpass("SET YOUR PASSWORD: ")
        my_dict[user_name] = user_password
        running = False
    elif user_response.upper() == "N":   
        run = True
        while run:
            print("PLZ LOGIN WITH VALID CREDENTIALS")
            username = input("PLZ ENTER YOUR NAME: ")
            userpassword = getpass.getpass("ENTER YOUR PASSWORD: ")
            if username in my_dict:
                if my_dict[username] == userpassword:                        
                    print("LOGIN SUCCESSFUL!")
                    run = False
                    running = False
                else:
                    print("INVALID CREDENTIALS..TRY AGAIN")
            else:
                print("INVALID USERNAME..TRY AGAIN")        
    else:
        print("INVALID INPUT")             

# OUR VARIABLES
outcomes = "Welcome to the world of searching knowledge and skills. At the end of the program you should be able to write and spell the alphabet, connect multiple alphabets to make a spelled word, write the names of things that surround you, and communicate through writing. You should also have the basic skills to perform well the rest of your education journey. Now, it is time to start the program, welcome!"
guidelines = "Hello! thank you for your interest in learning alphabet and you're welcome on Alpha_learning_app. This is a game that will help you to learn the aphabet. The game has 3 levels: level 1 for beginners, level 2 for intermediate, and level 3 which is the advanced level. At the end of each level you will be given a quiz which you must pass with at least 75% to continue to the next level. If you fail the quiz, you will have a chance to repeat again. Good luck"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
score_list = [0]
level_list = [1]
score1_list = [0]
score2_list = [0]
word_list = ['cat','dog','cup','bag','cow','den','goat','run','big','ball','play']


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
    user_option = input("WOULD YOU LIKE TO CONTINUE TO THE NEXT LEVEL? y/n ")
    if user_option.upper() == "Y":
        pass
    elif user_option.upper() == "N":
        print("quitting....")
        quit()
    else:
        print("INVALID INPUT")    

def check1_alphabet(score1_list):
    """Check if alphabet is correct"""
    r = RandomWords()
    word = r.get_random_word()     #returns a single random word
    for item in word:
        speak(item)
    speak(word)
        # Asks the user to input the alphabet he/she heard
    alpha_word = input("Enter the word you heard: ")
    if alpha_word.lower() == word:
        print("Correct!")
        score1_list.append((score1_list[-1] + 1))
        print(f"YOUR SCORE IS {(((score1_list[-1])/5) * 100)}%")
    else:
        print("Incorrect!")
        print(f"The correct word is: {word}")
        print(f"YOUR SCORE REMAINS {(((score1_list[-1])/5) * 100)}%")

def questions1(score1_list):
    for item in range(5):
        check1_alphabet(score1_list)
    return (((score1_list[-1])/5) * 100)

def score1_update():
    user_score = questions1(score1_list)
    if user_score >= 75 :
        speak("CONGRATULATIONS! YOU HAVE PASSED THIS LEVEL")
    else:
        speak("SORRY! YOU HAVE FAILED THIS LEVEL! TRY AGAIN")

def level_upgrade(level_list):
    level_list.append(level_list[-1] + 1)
    return level_list[-1]

def check_alphabet(score_list):
    """Check if alphabet is correct"""
    random_alphabet = random.choice(string.ascii_lowercase)
    speak(random_alphabet)
    # Asks the user to input the alphabet he/she heard
    alpha = input("Enter the alphabet you heard: ")
    if alpha.lower() == random_alphabet:
        print("Correct!")
        score_list.append((score_list[-1] + 1))
        print(f"YOUR SCORE IS {(((score_list[-1])/5) * 100)}%")
    else:
        print("Incorrect!")
        print(f"The correct alphabet is: {random_alphabet}")
        print(f"YOUR SCORE REMAINS {(((score_list[-1])/5) * 100)}%")

def speak_alphabet(alphabet):
    for item in alphabet:
        speak(item)
        print(item)

def respell():
    useroption = input("WOULD YOU LIKE US TO RESPELL THE ALPHABET?: Y/N")
    if useroption.lower() == 'y':
        speak_alphabet(alphabet) 
    elif useroption.lower() == 'n':
        pass
    else:
        print("INVALID INPUT")

def questions(score_list):
    for item in range(5):
        check_alphabet(score_list)
    return (((score_list[-1])/5) * 100) 

def score_update():
    user_score = questions(score_list)
    if user_score >= 75 :
        speak("CONGRATULATIONS! YOU HAVE PASSED THIS LEVEL")
        speak("GET READY FOR THE NEXT LEVEL")
        time.sleep(2)
        option()
        level_upgrade(level_list)
    else:
        speak("SORRY! YOU HAVE FAILED THIS LEVEL! TRY AGAIN")
        option2()   

def check2_alphabet(score2_list):
    """Check if alphabet is correct"""
    word = random.choice(word_list)
    for item in word:
        speak(item)
    speak(word)
        # Asks the user to input the alphabet he/she heard
    alpha_word = input("Enter the word you heard: ")
    if alpha_word.lower() == word:
        print("Correct!")
        score2_list.append((score2_list[-1] + 1))
        print(f"YOUR SCORE IS {(((score2_list[-1])/5) * 100)}%")
    else:
        print("Incorrect!")
        print(f"The correct word is: {word}")
        print(f"YOUR SCORE REMAINS {(((score2_list[-1])/5) * 100)}%")

def questions2(score2_list):
    for item in range(5):
        check2_alphabet(score2_list)
    return (((score2_list[-1])/5) * 100)

def score2_update():
    user_score = questions2(score2_list)
    if user_score >= 75 :
        speak("CONGRATULATIONS! YOU HAVE PASSED THIS LEVEL")
        speak("GET READY FOR THE NEXT LEVEL")
        option()
        level_upgrade(level_list)
    else:
        speak("SORRY! YOU HAVE FAILED THIS LEVEL! TRY AGAIN")
        option3()
        

def option2():
    user_option = input("WOULD YOU LIKE TO REPEAT THIS LEVEL? y/n ")
    if user_option.upper() == "Y":
        del score_list[-1]
        speak("THIS IS LEVEL ONE")
        speak("WE ARE GOING TO SPELL THE ALPHABET FOR YOU! PAY ATTENTION")
        time.sleep(2)
        print("GET READY FOR THE QUIZ: ")  
        time.sleep(2)
        speak_alphabet(alphabet)
        respell() 
        score_update()
        
    elif user_option.upper() == "N":
        print("quitting....")
        quit()
    else:
        print("INVALID INPUT")        

def option3():
    user_option = input("WOULD YOU LIKE TO REPEAT THIS LEVEL? y/n ")
    if user_option.upper() == "Y":
        del score2_list[-1]
        speak("THIS IS LEVEL TWO")
        speak("GET READY FOR THE QUIZ: ") 
        time.sleep(2)
        score2_update() 
    elif user_option.upper() == "N":
        print("quitting...")
        quit()
    else:
        print("INVALID INPUT")              


#out_come(outcomes)
#guide_line(guidelines)

# LEVEL 1
if level_list[-1] == 1 :
    speak("THIS IS LEVEL ONE")
    speak("WE ARE GOING TO SPELL THE ALPHABET FOR YOU! PAY ATTENTION")
    time.sleep(2)
    print("GET READY FOR THE QUIZ: ")  
    time.sleep(2)
    speak_alphabet(alphabet)
    respell() 
    score_update()
# LEVEL 2
if level_list[-1] == 2:
    speak("THIS IS LEVEL TWO")
    speak("GET READY FOR THE QUIZ: ") 
    time.sleep(2)
    score2_update() 

  #LEVEL 3
if level_list[-1] == 3:
    speak("THIS IS LEVEL THREE")
    speak("GET READY FOR THE QUIZ: ") 
    time.sleep(2)
    score1_update() 
