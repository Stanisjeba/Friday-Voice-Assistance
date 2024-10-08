Friday Voice Assistant
Description
Friday is a voice-controlled personal assistant powered by Python's speech_recognition and pyttsx3 libraries. This assistant listens for specific voice commands and performs Google searches based on the queries you provide. Additionally, it can enter an indefinite waiting state, only resuming when prompted. The assistant is responsive to the following commands:

"Friday start": Initiates the assistant.
"Friday search for <query>": Performs a Google search.
"wait": Pauses the assistant, waiting for the "begin" command.
"begin": Resumes after the assistant is paused.
"Friday stop": Terminates the assistant.
Friday is configured to respond using a female voice (if available on the system), providing a more personalized experience.

Features
Voice Commands:

Start the assistant with "Friday start".
Search Google with "Friday search for <query>".
Pause the assistant with "wait" and resume with "begin".
Terminate the session with "Friday stop".
Google Search Integration: You can search Google directly from voice commands.

Waiting State: You can put the assistant in a waiting mode, which stops it from accepting queries until the "begin" command is given.

Female Voice: The assistant speaks with a female voice (if available in the system).

Technologies Used
Python (v3.x)
speech_recognition: For recognizing voice commands.
pyttsx3: For text-to-speech functionality.
webbrowser: To open search results in a web browser.
Prerequisites
Before running the program, ensure you have the following libraries installed:

speech_recognition: For recognizing speech from the microphone.
pyttsx3: For text-to-speech conversion.
PyAudio: Required for audio input (microphone).
webbrowser: To open web search results.
You can install these using pip:

bash
Copy code
pip install speechrecognition pyttsx3 pyaudio
Installation
Clone the Repository:

Clone this repository to your local machine using:

bash
Copy code
git clone https://github.com/your-username/friday-voice-assistant.git
Install the Dependencies:

Navigate to the project directory and install the necessary Python packages:

bash
Copy code
cd friday-voice-assistant
pip install -r requirements.txt
If the requirements.txt file is not present, you can manually install the packages:

bash
Copy code
pip install speechrecognition pyttsx3 pyaudio
Check for Available Voices (Optional):

If the assistant’s voice is not female, you can check which voices are available on your system with the following snippet:

python
Copy code
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name, voice.id)
Once you identify a female voice, modify the code to use the correct voice ID.

Usage
Run the Program:

You can run the program using:

bash
Copy code
python friday_assistant.py
Interaction:

The assistant will wait for you to say "Friday start". After it starts, you can provide the following commands:

Search Google: Say "Friday search for <your query>". The assistant will perform a Google search and open the results in your default browser.
Pause the Assistant: Say "wait". The assistant will pause indefinitely.
Resume the Assistant: Say "begin". The assistant will resume listening for queries.
Terminate the Assistant: Say "Friday stop" to end the session.
Command List
"Friday start": Starts the voice assistant.
"Friday search for <query>": Conducts a Google search for the specified query.
"wait": Puts the assistant in an indefinite wait state.
"begin": Resumes after the assistant was paused.
"Friday stop": Stops the assistant.
Example Interaction
bash
Copy code
> (Assistant) Say 'Friday start' to begin.
> (User) Friday start
> (Assistant) Starting search mode.
> (User) Friday search for Python tutorials
> (Assistant) Searching for Python tutorials on Google...
   (Browser opens with the Google search results)
> (User) wait
> (Assistant) Waiting mode activated. Say 'begin' to continue.
> (User) begin
> (Assistant) Resuming search mode.
> (User) Friday stop
> (Assistant) Goodbye!
Known Issues
Voice Selection: The assistant attempts to select a female voice, but the availability of voices depends on your system's configuration. If no female voice is found, the default voice is used.

PyAudio Installation: Installing PyAudio can sometimes be tricky, especially on Windows systems. If you encounter issues, you may need to download the appropriate .whl file from here and install it manually using:

bash
Copy code
pip install <path-to-pyaudio-wheel>
Contribution
If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your changes. Any improvements or bug fixes are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

