import wikipedia
import requests
import re
from spellchecker import SpellChecker
from transformers import pipeline
from fuzzywuzzy import fuzz, process

# Initialize spell checker
spell = SpellChecker()

# Load intent classification model
nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Keywords for fuzzy matching
disease_keywords = [
    "cold", "flu", "diabetes", "asthma", "headache", "fever",
    "covid", "hiv", "aids", "malaria", "hypertension", "allergy",
    "migraine", "infection", "cancer", "cough", "pain", "sore throat",
    "diarrhea", "vomiting", "rash", "dehydration"
]

# Spelling correction with fallback
def correct_spelling(text):
    corrected = []
    for word in text.split():
        # Prioritize medical keywords
        best_match = process.extractOne(word, disease_keywords, scorer=fuzz.ratio)
        if best_match and best_match[1] > 80:
            corrected.append(best_match[0])
        else:
            correction = spell.correction(word)
            corrected.append(correction if correction else word)
    return " ".join(corrected)


# Fuzzy match disease name
def fuzzy_find_disease(user_input):
    result = process.extractOne(user_input, disease_keywords, scorer=fuzz.partial_ratio)
    if result:
        match, score = result[0], result[1]
        return match if score > 80 else None
    return None

# Get drug recommendations from FDA
def get_drug_recommendations(symptom):
    url = f"https://api.fda.gov/drug/label.json?search={symptom}&limit=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            drugs = response.json().get("results", [])
            if not drugs:
                return "No relevant drug information found."

            output = []
            for drug in drugs:
                name = drug.get("openfda", {}).get("brand_name", ["Unnamed Drug"])[0]
                desc = drug.get("description") or drug.get("indications_and_usage")

                if not desc:
                    continue

                short_desc = desc[0] if isinstance(desc, list) else desc
                short_desc = short_desc[:300].split(".")[0] + "."
                output.append(f"{name}: {short_desc}")

            return "\n\n".join(output) if output else "No usable descriptions found for the drugs."
        else:
            return f"API request failed with status code {response.status_code}."
    except Exception as e:
        return f"Error while contacting drug info service: {str(e)}"

# Get summary from Wikipedia
def get_disease_info(disease):
    try:
        summary = wikipedia.summary(disease, sentences=2, auto_suggest=False)
        return f"Here's some information about {disease}:\n{summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:5])
        return f"'{disease}' is ambiguous. Did you mean: {options}?"
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find information on '{disease}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Core logic to process user message
def process_medical_query(user_input):
    user_input_lower = user_input.lower().strip()

    # Handle exit
    if user_input_lower in ["bye", "quit", "exit", "goodbye", "see you"]:
        print("Assistant: Goodbye! Stay healthy!")
        exit()

    # Match info-related phrases with regex
    if any(phrase in user_input_lower for phrase in ["tell me about", "what is", "explain", "explain about", "info about"]):
        match = re.search(r"(?:tell me about|what is|explain(?: about)?|info about)\s+(.*)", user_input_lower)
        disease_name = match.group(1).strip() if match else ""
        if not disease_name:
            response = "Please specify a disease or symptom."
        else:
            response = get_disease_info(disease_name)
        print(f"Assistant: {response}")
        return

    # Classify intent
    labels = ["greeting", "symptoms", "disease", "drug recommendation", "general_info"]
    result = nlp(user_input, candidate_labels=labels)
    top_intent = result['labels'][0]
    print(f"[DEBUG] Top intent: {top_intent}")

    # Handle intent
    if top_intent == "greeting":
        response = "Hello! How can I help you today?"
    elif top_intent in ["symptoms", "disease"]:
        disease_name = fuzzy_find_disease(user_input) or user_input
        response = get_disease_info(disease_name)
    elif top_intent == "drug recommendation":
        symptom = fuzzy_find_disease(user_input) or user_input
        response = get_drug_recommendations(symptom)
    else:
        response = "I'm not sure how to help with that. You can ask about symptoms, diseases, or drug suggestions."

    print(f"Assistant: {response}")

# Main chatbot loop
def chatbot():
    while True:
        raw_input = input("You: ")
        corrected_input = correct_spelling(raw_input)
        process_medical_query(corrected_input)

# Run chatbot
if __name__ == "__main__":
    print("🩺 Welcome to the Medical Assistant. Type 'quit' anytime to exit.")
    chatbot()

