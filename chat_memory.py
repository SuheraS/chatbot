import datetime

class ChatMemory:
    def __init__(self, max_turns=3):
        self.max_turns = max_turns
        self.history = []

    def add_turn(self, user_input, bot_response):
        timestamp = datetime.datetime.now().strftime("%H:%M")
        self.history.append(f"[{timestamp}] You: {user_input}\n[{timestamp}] Bot: {bot_response}")
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return "\n".join(self.history)