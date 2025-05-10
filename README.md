# 🧠 AI Assistant Project

This project contains three intelligent systems built using Python, NLP, and Speech technologies:

## 🔍 1. Sentiment Analysis
- Identifies if a sentence expresses a **positive** or **negative** sentiment.
- Fetches relevant news articles based on sentiment.
- Uses Hugging Face Transformers and NewsAPI.

## 🎙️ 2. Voice Assistant
- Listens to voice commands.
- Responds with weather updates, jokes, or executes Google searches.
- Uses SpeechRecognition, pyttsx3, and OpenWeatherMap API.

## 🏥 3. Healthcare Chatbot
- Answers queries about diseases and symptoms.
- Suggests drug recommendations using FDA Drug API.
- Uses fuzzy matching, Wikipedia, and Hugging Face Transformers.

## 🚀 How to Run
1. Install dependencies:
pip install -r requirements.txt

sql
Copy
Edit
2. Run each task using:
python task_1_sentiment_analysis/sentiment_analysis.py
python task_2_voice_assistant/voice_assistant.py
python task_3_healthcare_chatbot/healthcare_chatbot.py

markdown
Copy
Edit

## 🔑 API Keys
- NewsAPI: [https://newsapi.org](https://newsapi.org)
- OpenWeatherMap: [https://openweathermap.org/api](https://openweathermap.org/api)
- FDA Drug API: No key needed

## 📂 Project Structure
AI-Assistant-Project/
├── sentiment_analysis.py
├── voice_assistant.py
├── healthcare_chatbot.py
├── requirements.txt
└── README.md