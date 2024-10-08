import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice to female (try to set a female voice from available voices)
voices = engine.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower() or 'female' in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break  # Use the first female voice found

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice command with 15-second timeout
def listen(timeout=15, phrase_time_limit=15):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        
        try:
            # Listen for a maximum of 15 seconds (or custom timeout) and limit phrase length to 15 seconds
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"{query}")
            speak(f"{query}")
            return query.lower()  # Convert query to lowercase for easier comparisons
        except sr.WaitTimeoutError:
            print("Listening timed out waiting for a phrase.")
            speak("Listening timed out.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            speak("Sorry, I didn't get that.")
            return None
        except sr.RequestError:
            print("Network error.")
            speak("Network error.")
            return None

# Function to search Google
def search_on_google(query):
    if query.startswith("friday search for"):
        search_query = query.replace("friday search for", "").strip()
        # Format the search query URL for Google search
        search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        print(f"Searching for {search_query} on Google...")
        speak(f"Searching for {search_query} on Google...")
        # Open the default web browser with the search URL
        webbrowser.open(search_url)
        return True  # Continue the loop
    else:
        speak("Please start your query with 'Friday search for'.")
        return True  # Continue the loop

# Function to wait for the "Friday start" command
def wait_for_start_command():
    speak("Say 'Friday start' to begin.")
    while True:
        command = listen()
        if command == "friday start":
            speak("Starting search mode.")
            break
        else:
            speak("Waiting for 'Friday start' command.")

# Function to wait indefinitely for "begin" after "wait"
def wait_for_begin_command():
    speak("Waiting mode activated. Say 'begin' to continue.")
    while True:
        command = listen(timeout=None, phrase_time_limit=15)  # No timeout to wait indefinitely
        if command == "begin":
            speak("Resuming search mode.")
            break

# Main function to handle the voice assistant process
def main():
    wait_for_start_command()  # Wait for 'Friday start' to begin

    keep_going = True
    while keep_going:
        query = listen()
        if query:
            if query == "friday stop":
                speak("Thank you! Goodbye ! ")
                keep_going = False
            elif query == "wait":
                wait_for_begin_command()  # Go into waiting mode
            else:
                keep_going = search_on_google(query)
        else:
            speak("Let's try again.")

if __name__ == "__main__":
    main()
