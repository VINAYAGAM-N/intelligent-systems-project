# 🧠 AI Assistant Project

This project contains three intelligent systems built using Python, NLP, and Speech technologies:

---

### 🔍 1. Sentiment Analysis
Identifies if a sentence expresses a positive or negative sentiment.  
Fetches relevant news articles based on sentiment.  
Uses Hugging Face Transformers and NewsAPI.

#### Sentiment Output

- **Positive Sentiment:**
  ![Positive Sentiment](assets/sentiment_output_positive.png)  
  *(This is a screenshot showing positive sentiment output)*

- **Negative Sentiment:**
  ![Negative Sentiment](assets/sentiment_output_negative.png)  
  *(This is a screenshot showing negative sentiment output)*

#### How It Works
- Sentiment analysis is performed using the Hugging Face Transformers library.
- It fetches related news articles using NewsAPI based on the sentiment (positive or negative).

---

### 🎙️ 2. Voice Assistant
Listens to voice commands.  
Responds with weather updates, jokes, or executes Google searches.  
Uses SpeechRecognition, pyttsx3, and OpenWeatherMap API.

#### Demo Video
![Voice Assistant image](assets/voice_assistant.png)  
*(This is a screenshot showing the Voice Assistant responding to commands)*

Or, you can provide a direct link to the video:
[Watch the Voice Assistant Demo](assets/voice_assistant_demo.mp4)

#### How It Works
- The assistant listens to user voice commands using SpeechRecognition.
- It responds via text-to-speech (TTS) using pyttsx3.
- It can fetch weather details or perform Google searches based on user input.

---

### 🏥 3. Healthcare Chatbot
Answers queries about diseases and symptoms.  
Suggests drug recommendations using the FDA Drug API.  
Uses fuzzy matching, Wikipedia, and Hugging Face Transformers.

#### Sample Output
![Healthcare Chatbot Output](assets/chatbot_output.png)  
*(This is a screenshot showing the chatbot's response to a disease query)*

#### How It Works
- The chatbot uses fuzzy matching for disease names and symptoms.
- It provides Wikipedia-based information on diseases and recommends drugs using the FDA Drug API.

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run each task using the following commands:

bash
Copy
Edit
python task_1_sentiment_analysis/sentiment_analysis.py
python task_2_voice_assistant/voice_assistant.py
python task_3_healthcare_chatbot/healthcare_chatbot.py
🔑 API Keys
NewsAPI: https://newsapi.org

OpenWeatherMap: https://openweathermap.org/api

FDA Drug API: No API key needed

###📂 Project Structure

AI-Assistant-Project/
├── sentiment_analysis.py
├── voice_assistant.py
├── healthcare_chatbot.py
├── assets/
│   ├── sentiment_output_positive.png
│   ├── sentiment_output_negative.png
│   ├── voice_assistant_demo.mp4
│   ├── voice_assistant.png
│   └── chatbot_output.png
├── requirements.txt
└── README.md
