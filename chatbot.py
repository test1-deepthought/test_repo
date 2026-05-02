"""
Simple Rule-Based Chatbot in Python

A pattern-matching chatbot that responds to greetings, questions about itself,
basic small talk, and farewells. Uses regular expressions for flexible matching.
"""

import re
import random


class ChatBot:
    """A rule-based chatbot with pattern matching capabilities."""

    def __init__(self, name="ChatBot"):
        self.name = name
        self.patterns = [
            # (regex_pattern, list_of_possible_responses)
            (r"\bhello\b|\bhi\b|\bhey\b|\bgreetings\b", [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!",
                "Greetings! How are you doing?",
            ]),
            (r"how are you", [
                "I'm doing great, thanks for asking!",
                "I'm just a program, but I'm running smoothly!",
                "All systems operational! How about you?",
            ]),
            (r"what('?s| is) your name", [
                f"My name is {name}. Nice to meet you!",
                f"I go by {name}. What's yours?",
                f"I'm {name}, your friendly chatbot!",
            ]),
            (r"who (are|made|created) you", [
                "I was created as a demonstration of a simple Python chatbot.",
                "A Python programmer built me using pattern matching!",
                "I'm the result of some Python code and regular expressions.",
            ]),
            (r"what can you do", [
                "I can chat with you, answer simple questions, and keep you company!",
                "I'm a rule-based chatbot, so I can respond to greetings, answer basic questions, and more!",
                "I can have conversations, tell you about myself, and even tell jokes!",
            ]),
            (r"tell me a joke", [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the Python programmer squeeze the toothpaste? Because the tube said 'apply from the middle'!",
                "What do you call a bear with no teeth? A gummy bear!",
            ]),
            (r"\b(thanks|thank you)\b", [
                "You're welcome!",
                "Happy to help!",
                "Anytime!",
                "No problem at all!",
            ]),
            (r"\b(bye|goodbye|see you|farewell)\b", [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! It was nice chatting with you.",
                "Farewell! Come back anytime!",
            ]),
            (r"\b(weather|temperature)\b", [
                "I don't have access to weather data, but I hope it's nice where you are!",
                "I can't check the weather, but you could try a weather app!",
            ]),
            (r"\b(love|like) you\b", [
                "Aww, that's sweet!",
                "Right back at you!",
                "You're pretty great yourself!",
            ]),
            (r"my name is (\w+)", [
                "Nice to meet you, {0}!",
                "Hello {0}, that's a lovely name!",
                "Great to know you, {0}!",
            ]),
            (r"i('?m| am) (sad|unhappy|upset|depressed)", [
                "I'm sorry to hear that. Want to talk about it?",
                "That's tough. Sometimes sharing helps — I'm here to listen.",
                "I hope things get better soon. I'm here for you!",
            ]),
            (r"i('?m| am) (happy|glad|great|good|wonderful)", [
                "That's wonderful to hear!",
                "Awesome! Keep that positive energy going!",
                "Glad to hear it! What's making you happy?",
            ]),
        ]
        self.default_responses = [
            "Interesting... tell me more!",
            "I see. What else is on your mind?",
            "That's fascinating! Can you elaborate?",
            "Hmm, I'm not sure how to respond to that. Try asking me something else!",
            "I'm still learning. Could you rephrase that?",
        ]

    def respond(self, user_input: str) -> str:
        """Generate a response based on the user's input."""
        user_input = user_input.strip().lower()
        if not user_input:
            return "You didn't say anything! Type something and I'll respond."

        for pattern, responses in self.patterns:
            match = re.search(pattern, user_input)
            if match:
                response = random.choice(responses)
                # Substitute captured groups if any
                if match.groups():
                    try:
                        response = response.format(*match.groups())
                    except (IndexError, KeyError):
                        pass
                return response

        return random.choice(self.default_responses)

    def run(self):
        """Start an interactive chat session in the terminal."""
        print(f"=" * 50)
        print(f"  Welcome to {self.name}!")
        print(f"  Type 'quit', 'exit', or 'bye' to end the conversation.")
        print(f"=" * 50)
        print()
        print(f"{self.name}: Hello! I'm {self.name}. How can I help you?")
        print()

        while True:
            try:
                user_input = input("You: ")
            except (EOFError, KeyboardInterrupt):
                print(f"\n{self.name}: Goodbye! Take care!")
                break

            if user_input.lower() in ("quit", "exit", "bye", "goodbye"):
                print(f"{self.name}: Goodbye! It was nice chatting with you!")
                break

            response = self.respond(user_input)
            print(f"{self.name}: {response}")
            print()


if __name__ == "__main__":
    bot = ChatBot(name="ChatBot")
    bot.run()
