This project is an AI Voice Assistant written in Python, capable of recognizing voice commands, executing certain system tasks like opening a web browser, and answering questions using the power of AI (AI/ML service API with ).  
The assistant is designed to help you automate routine tasks, combining voice recognition, Natural Language Processing (NLP), and AI.  

**Features**  

Voice Command Recognition -> The assistant listens to your voice and processes commands.  
AI-Powered Question Answering -> Using an AI model (like Claude 3.5 Sonnet) to answer questions, provide information  
Custom Commands -> You can add additional commands to suit your needs.  

**Technologies Used**  

Python -> The core programming language for this project.  
SpeechRecognition -> For converting speech to text.  
pyttsx3 -> A text-to-speech conversion library for responding back to the user.  
AI/ML API -> To provide AI-based answers and conversations. (https://aimlapi.com)  

**How It Works**  
The AI Assistant will start by listening to your commands through the microphone.  
You can give it voice commands like:  
  "Open browser" – It will open your default web browser.  
  "Open youutbe" – It will open your youtube.  
  "exit" - will close the Assitant  

**Customization**  

You can customize the assistant to handle more commands by modifying the execite_command() function  
And adding the keyword(s) for the identification of the command in the elif statement in the main() function on line 86

Add your keyword(s) for the identification of the command with another "or" operator  
```python
elif "open browser" in spoken_text or "open youtube" in spoken_text:
```

**LICENSE**  

This project is licensed under the MIT License.  


  
