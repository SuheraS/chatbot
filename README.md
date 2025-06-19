# Local Command-Line Chatbot using Hugging Face

This is a local chatbot built for the Machine Learning Internship Task. It runs in the terminal and uses a Hugging Face Question Answering model to answer user queries. The chatbot also remembers recent messages using a short-term memory buffer.

---

## Features

- Runs locally with no internet or API required
- Built using `transformers` and `torch`
- Answers factual questions like country capitals
- Maintains memory of the last 3 turns using a sliding window
- Supports `/clear` to reset memory and `/exit` to quit
- Timestamped conversation turns for better UX

---

## Project Structure

chatbot/
├── interface.py # Main CLI loop and chatbot logic
├── model_loader.py # Loads the QA model
├── chat_memory.py # Stores recent conversations
├── README.md # Project documentation


---

## Installation

1. Make sure you have Python 3.8+ installed
2. Install required libraries:

pip install transformers torch



---

## Running the Chatbot

Navigate to the folder and run:

python interface.py


You’ll see:

Chatbot is running! Type '/exit' to quit or '/clear' to reset memory.


---

## Example Interaction

You: What is the capital of France?
Bot: Paris

You: And what about Italy?
Bot: Rome

You: /clear
Bot: Memory cleared!

You: /exit
Bot: Exiting chatbot. Goodbye!


---

## Notes

- The chatbot uses a default context with facts about countries and capitals.
- It uses a Question-Answering model (`distilbert-base-uncased-distilled-squad`) from Hugging Face.
- All conversation is remembered in short-term memory (last 3 turns) and used as context.
- This is not a generative chatbot — it extracts answers from the memory or default context.

---

## Built By

**Suhera Siddiqui**  