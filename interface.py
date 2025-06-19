from model_loader import load_model

from chat_memory import ChatMemory

def main():
    chatbot = load_model()
    memory = ChatMemory(max_turns=3)

    print("Chatbot is running! Type '/exit' to quit or '/clear' to reset memory.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        if user_input.lower() == "/clear":
            memory = ChatMemory(max_turns=3)
            print("Bot: Memory cleared!\n")
            continue

        # Get recent memory context
        context = memory.get_context()

        # If no context yet, use default facts to help model answer
        if not context.strip():
            context = (
                "France is a country in Europe. Its capital is Paris. "
                "Italy is a country in Europe. Its capital is Rome. "
                "India is a country in Asia. Its capital is New Delhi. "
                "Japan is a country in Asia. Its capital is Tokyo. "
                "The USA is a country in North America. Its capital is Washington, D.C."
            )

        try:
            response = chatbot({
                'question': user_input,
                'context': context
            })
            answer = response['answer']
        except Exception as e:
            answer = "Sorry, I couldn't understand that."

        memory.add_turn(user_input, answer)
        print(f"Bot: {answer}\n")

if __name__ == "__main__":
    main()
