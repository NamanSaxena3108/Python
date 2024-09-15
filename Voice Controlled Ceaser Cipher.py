#python program for voice controlled caeser cyphe
from ceaser_cipher_art import logo
import speech_recognition as sr     #module for converting speech to text
import pyttsx3                      #module for converting text to speech

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

# Function to convert text to speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

r=sr.Recognizer()

print("Hello! Welcome to Caeser Cypher")
SpeakText("Hello! Welcome to Caeser Cypher")

print("Please tell your choice : Encode or Decode")
SpeakText("Please tell your choice : Encode or Decode")
try:
		
	# use the microphone as source for input.
    with sr.Microphone() as source2:
			
	    # wait for a second to let the recognizer
	    # adjust the energy threshold based on
	    # the surrounding noise level 
        r.adjust_for_ambient_noise(source2, duration=0.1)
			
	    #listens for the user's input 
        audio2 = r.listen(source2)
	
	    # Using google to recognize audio
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()

        print(MyText)
        SpeakText(MyText)
			
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
	
except sr.UnknownValueError:
    print("unknown error occurred")
else:
    if "encode" in MyText:
        print("Enter shift count (1-25):")
        SpeakText("Enter shift count (1-25):")
        key = int(input())
        def caesar(start_text ,shift_amount):
            end_text= ""
            for char in start_text:
                if char in alphabet:
                    position = alphabet.index(char)
                    new_position = position + shift_amount
                    end_text += alphabet[new_position]
                else:
                    end_text += char
            print(f"Here is the encoded result: {end_text}")
            SpeakText(f"Here is the encoded result: {end_text}")
        should_end = False 

        while not should_end:
            print("Enter the message you want to encode:")
            SpeakText("Enter the message you want to encode:")
            text = input().lower()
            caesar(start_text=text , shift_amount=key)
            print("type 'yes' if you want to go again. otherwise type'no'.\n")
            SpeakText("type 'yes' if you want to go again. otherwise type'no'.")
            restart = input()
            if restart == "no":
                should_end = True
    if "decode" in MyText:
        print("Enter shift count (1-25):")
        SpeakText("Enter shift count (1-25):")
        key = int(input())
        key*=-1
        def caesar(start_text ,shift_amount):
            end_text= ""
            for char in start_text:
                if char in alphabet:
                    position = alphabet.index(char)
                    new_position = position + shift_amount
                    end_text += alphabet[new_position]
                else:
                    end_text += char
            print(f"Here is the encoded result: {end_text}")
            SpeakText(f"Here is the encoded result: {end_text}")
        should_end = False 
        
        while not should_end:
            print("Enter the message you want to encode:")
            SpeakText("Enter the message you want to encode:")
            text = input().lower()
            key = key % 26
            caesar(start_text=text , shift_amount=key)
            restart = input("type 'yes' if you want to go again. otherwise type'no'.\n")
            if restart == "no":
                should_end = True
                print("Goodbye")
