from transformers import pipeline

def load_model():
    return pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
