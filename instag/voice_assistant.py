import speech_recognition as sr
from gtts import gTTS,gTTSError
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import requests

state = "null"

try:
    pygame.mixer.init()

except:
    state = "something went wrong"
    print("something went wrong")

def speech_to_text():
    global state
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        state = "listenig..."
        print("listenig...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        
        audio = recognizer.listen(source,10,4)  # Listen to audio
        state = "recognizing"

        try:
            text = recognizer.recognize_google(audio)  # Convert audio to text using Google's speech recognition
            state = "processing:"+"*"+text+"*"
            return text.lower()
        except sr.UnknownValueError:
            a = "Sorry, I couldn't understand what you said"
            state = a
            print(a)
            return 0
        except sr.RequestError as e:
            a = "Please check your internet connection and try again later"
            state = a
            print(a)
            return 1
        

def text_to_speech(text, output_path = "files\output.mp3"):
    
    try:
        tts = gTTS(text)
        tts.save(output_path)

    except gTTSError as e:
        print("Network error,Please check your network connection")
        return
    except requests.exceptions.RequestException as e:
        print("Network error,Please check your network connection")
        return

# Load the music file
    music_file =output_path
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)

# Set the volume (optional)
    pygame.mixer.music.set_volume(1.0)  # Adjust the volume as needed (0.0 to 1.0)

# Play the music
    pygame.mixer.music.play()

# Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

# Quit pygame when done
    pygame.quit()

    
if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Speech to Text")
        print("2. Text to Speech")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            speech_to_text()
        elif choice == "2":
            text = input("Enter the text to convert to speech: ")
            text_to_speech(text)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
