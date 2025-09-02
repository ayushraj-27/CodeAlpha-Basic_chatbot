import random
from datetime import datetime


def chatbot():
    greetings = ["Hi!", "Hello!", "Hey there!", "Hi, nice to meet you!"]
    mood_responses = [
        "I'm doing great! How about you?",
        "I'm fine, thanks for asking!",
        "Feeling awesome! What about you?"
    ]
    goodbye_responses = ["Goodbye!", "See you later!", "Bye! Take care!"]

    print(" Chatbot: Welcome! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print(" Chatbot:", random.choice(greetings))
        elif "how are you" in user_input:
            print(" Chatbot:", random.choice(mood_responses))
        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f" Chatbot: Current time is {now}")
        elif "bye" in user_input:
            print(" Chatbot:", random.choice(goodbye_responses))
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()

