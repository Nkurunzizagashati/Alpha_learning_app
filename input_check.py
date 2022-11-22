import sys
import string
import random
import os
import time
import speech_recognition as sr
from gtts import gTTS

class Alphabets:
    """Alphabets class"""


    def __init__(self, alphabet, alpha):
        """Constructor for Alphabets class"""
        self.alphabet = alphabet
        self.alpha = alpha

    def audio_alphabet(self):
        """Audio of all alphabets"""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alpha = gTTS(text=self.alphabet, lang='en')
        alpha.save("alphabet.mp3")
        os.system("alphabet.mp3")

    def check_alphabet(self):
        """Check if alphabet is correct"""
        random_alphabet = random.choice(string.ascii_lowercase)
        random_alphabet = gTTs(text=random_alphabet, lang='en')
        random_alphabet.save("random_alphabet.mp3")
        os.system("random_alphabet.mp3")
        # Asks the user to input the alphabet he/she heard
        self.alpha = input("Enter the alphabet you heard: ")
        if self.alpha == random_alphabet:
            print("Correct!")
        else:
            print("Incorrect!")
            print("The correct alphabet is: ", random_alphabet)


Round1 = Alphabets("alphabet1", "alpha1")
Round1.audio_alphabet()
Round1.check_alphabet()
