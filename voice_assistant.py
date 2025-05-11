import speech_recognition as sr
import pyttsx3
import requests
import datetime
import pyjokes
import webbrowser
import random

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down.")
            speak("Sorry, the service is down.")
            return None

def get_weather_data():
    api_key = "API_KEY"  # Replace with your API key
    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data["cod"] == "404":
        speak("Sorry, I could not get the weather data.")
    else:
        main_data = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temperature = main_data["temp"] - 273.15
        speak(f"The weather in {city} is {weather_desc} with a temperature of {temperature:.2f}°C.")

def get_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")
    speak(f"The current time is {time_str} and today's date is {date_str}.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def open_website(url, name="the website"):
    speak(f"Opening {name}.")
    webbrowser.open(url)

# Command mappings
command_mappings = {
    "greeting": {
        "inputs": ["hello", "hi", "hey", "good morning", "good evening", "vanakkam", "eppadi irukka", "hi da"],
        "responses": ["Hello! How can I help you?", "Hi there!", "Vanakkam! Enna vishayam?", "Hey! Ready to assist."]
    },
    "quit": {
        "inputs": ["quit", "exit", "close", "stop", "bye", "goodbye", "poitu varen", "seri po"],
        "responses": ["Goodbye! Take care.", "See you later!", "Exiting. Have a nice day!", "Poitu varen!"]
    },
    "thanks": {
        "inputs": ["thanks","thank" ,"thank you", "nandri", "thanks da", "thank you bro"],
        "responses": ["You're welcome!", "No problem!", "Anytime!", "Glad to help!"]
    },
    "help": {
        "inputs": ["help","help me" "what can you do", "show commands","what you do", "commands"],
        "responses": [
            "I can tell jokes, fetch weather, tell time, search the web, open Google or YouTube, and more!",
            "Try asking me to tell a joke, get the weather, or search something.",
            "I'm here to help. Ask me anything like time, joke, or open a website."
        ]
    }
}

def process_command(command):
    command = command.lower()

    # Generic command mappings
    for category, data in command_mappings.items():
        if any(phrase in command for phrase in data["inputs"]):
            speak(random.choice(data["responses"]))
            if category == "quit":
                exit()
            return

    # Weather
    if "weather" in command:
        speak("Fetching the weather for you.")
        get_weather_data()

    # Time
    elif "time" in command:
        get_time()

    # Joke
    elif "joke" in command:
        tell_joke()

    # Open Google
    elif "open google" in command:
        open_website("https://www.google.com", "Google")

    # Open YouTube
    elif "open youtube" in command:
        open_website("https://www.youtube.com", "YouTube")

    # Generalized Google Search with English + Tanglish triggers
    else:
        search_triggers = [
            # English
            "search for", "look up", "find", "google", "search about", 
            "search on google", "can you search", "check this",

            # Tanglish
            "thedu", "google la paaru", "find pannunga", "google pannu",
            "check pannunga", "paathu sollu", "edhu thedu", 
            "kandu pidichu sollu", "search pannu da", "google la thedu"
        ]

        for trigger in search_triggers:
            if trigger in command:
                search_query = command.split(trigger)[-1].strip()
                if search_query:
                    speak(f"Searching Google for {search_query}")
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
                else:
                    speak("What should I search for?")
                return

        # Unknown command
        speak("I'm sorry, I don't recognize that command.")

def start_voice_assistant():
    while True:
        command = recognize_speech()
        if command:
            process_command(command)

# Start the assistant
start_voice_assistant()
