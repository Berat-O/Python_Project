import random

responses = [
    "Yes, definitely!",
    "No, not at all.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Without a doubt.",
    "Better not tell you now."
]

def magic_8_ball():
    """Simple CLI Magic 8 Ball game."""

    print("🎱 Welcome to Magic 8 Ball 🎱")

    while True:
        question = input("\nAsk a question (or type 'quit'): ")

        if question.lower() == "quit":
            print("Goodbye 👋")
            break

        print("Thinking...")
        print(random.choice(responses))

if __name__ == "__main__":
    magic_8_ball()