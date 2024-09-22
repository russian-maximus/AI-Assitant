from openai import OpenAI
import webbrowser
import speech_recognition as sr
import pyttsx3


AI_API_KEY = #place yout AI/ML API key

#Variables for AI/ML API
base_url = "https://api.aimlapi.com/v1"
api_key = AI_API_KEY
system_prompt = "You are a world-class AI assistant who knows everything and is an expert in every possible question that I give to you."
 
 #establish api connection with AI
api = OpenAI(api_key=api_key, base_url=base_url)

# Initialize TTS engine
engine = pyttsx3.init()

#Voice settings
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#for voice in engine.getProperty('voices'):
 #   print(voice)

# Initialize the SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Function to execute system commands
def execute_command(command):
    if "open browser" in command:
        webbrowser.open('https://www.google.com')
        return "Opening browser."
    elif "open youtube" in command:
        webbrowser.open('https://www.youtube.com')
        return "Opening Youtube."
    else:
        return "Command not recognized."

# Function to interact with AI API
def get_AI_response(user_prompt):
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2", #you can choose a diffrent model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=420,
    )

    response = completion.choices[0].message.content

    print("User:", user_prompt)
    print("AI:", response)
    return response

# Function to listen and recognize speech 
def listen_to_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio) 
            print(f"Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that. Please try again."

# Function to speak using TTS
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
def main():

    while True:
        spoken_text = listen_to_speech()
        if "exit" in spoken_text:
            speak("Goodbye!")
            break

        elif "open browser" in spoken_text or "shutdown" in spoken_text:
            response = execute_command(spoken_text)

        elif "open youtube" in spoken_text:
            response = execute_command(spoken_text)
        
        elif spoken_text == "Sorry, I didn't catch that. Please try again.":
            speak("Sorry, I didn't catch that. Please try again.")

        else:
            response = get_AI_response(spoken_text)

        speak(response)

#start
if __name__ == "__main__":
    main()
