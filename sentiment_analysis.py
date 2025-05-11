from transformers import pipeline
import requests

# Load pre-trained sentiment analysis pipeline
nlp = pipeline("sentiment-analysis")

# Function to analyze sentiment
def analyze_sentiment(text):
    result = nlp(text)
    sentiment = result[0]['label']
    return sentiment

# Function to fetch related news based on sentiment
def fetch_related_news(sentiment):
    sentiment_query = "positive" if sentiment == "POSITIVE" else "negative"
    url = f"https://newsapi.org/v2/everything?q={sentiment_query}&apiKey=API_KEY"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])
    
    if articles:
        return [article['title'] for article in articles[:3]]  # Return top 3 articles
    return ["No related news found."]

# Real-time interaction: User input for sentiment analysis
def sentiment_analysis():
    user_input = input("Please enter your sentence: ")  # Real-time user input
    sentiment = analyze_sentiment(user_input)
    print(f"Sentiment: {sentiment}")
    print()
    
    # Fetch related news based on sentiment
    related_news = fetch_related_news(sentiment)
    print("Related News based on sentiment:")
    for news in related_news:
        print(f"- {news}")

# Start real-time sentiment analysis
sentiment_analysis()
