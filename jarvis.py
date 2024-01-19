import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


#Initialize text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0],id)

#Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_bing(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def create_todo_list():
    speak("what do you want to add to your list?")
    task = recognize_speech()
    with open('todo.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {task}\n")
    speak("task add!")

def search_web():
    speak("What would you like to look for?")
    query = recognize_speech()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"The results for {query}.")

def set_reminder():
    speak("What should I remember?")
    task = recognize_speech()
    speak("In how many minutes?")
    mins = recognize_speech()
    mins = int(mins)
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=mins)
    with open('reminders.txt', 'a') as f:
        f.write(f"{reminder_time} - {task}\n")
    speak(f"Defined {mins}")

def main():
    speak("Hello! I'm your personal assistant. How can I assist you today?")
    conversation_history = []

    while True:
        query = recognize_speech().lower()
        conversation_history.append(query)

        if 'create a list task' in query:
            create_todo_list()

        elif 'search in web' in query:
            search_web()

        elif 'create a reminder' in query:
            set_reminder()

        elif "stop" in query or "exit" in query:
            speak("Goodbye! If you need anything, I'll be here.")
            break

        elif 'how are you' in query:
            speak("I'm just a computer program, but thanks for asking! How can I assist you today?")

        elif 'tell me a joke' in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")

        else:
            speak("I'm sorry, I didn't quite catch that. Is there something else I can help you with?")

main()
