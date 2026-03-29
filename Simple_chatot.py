import random

responses = {
    "hello": [
        "Hello! How can I help you today?",
        "Hi there! Nice to see you.",
        "Hey! What’s up?"
    ],
    "how are you": [
        "I'm doing great, thanks for asking!",
        "All systems running smoothly!",
        "I'm just a program, but feeling awesome!"
    ],
    "what is your name": [
        "I'm a simple Python chatbot.",
        "You can call me PyBot.",
        "I don’t have a fancy name yet!"
    ],
    "bye": [
        "Goodbye! Have a nice day.",
        "See you later!",
        "Bye! Take care."
    ],
    "default": [
        "I'm not sure how to respond to that.",
        "Could you rephrase that?",
        "Hmm, I don’t understand. Try asking differently."
    ]
}

def chatBot():
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("ChatBot: Thank you for using this chatbot!")
            break
        if user_input in responses:
            reply = random.choice(responses[user_input])
        else:
            reply = random.choice(responses["default"])
        print(f"ChatBot: {reply}")

chatBot()
