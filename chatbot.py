import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

# Store user name
user_name = ""

# Chatbot logic function
def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey", "assalamualaikum"]
    greeting_responses = [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any help?",
        "Wa Alaikum Assalam! How can I help you?"
    ]

    # Exit
    if user_input in ["exit", "bye", "quit", "allah hafiz"]:
        return "Goodbye! Take care 😊"

    # Greetings
    elif any(word in user_input for word in greetings):
        return random.choice(greeting_responses)

    # Name handling
    elif "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip()
        return f"Nice to meet you, {user_name}! 😊"

    elif "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name}!"
        return "I don't know your name yet. Tell me!"

    # Small talk
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊 What about you?"

    elif "what's up" in user_input or "what are you doing" in user_input:
        return "Just chatting with you 😄"

    elif "i am fine" in user_input or "i am good" in user_input:
        return "That's great to hear! 😊"

    elif "i am sad" in user_input or "i feel bad" in user_input:
        return "I'm sorry to hear that 💙 Things will get better!"

    # Study related
    elif "help me study" in user_input or "study" in user_input:
        return "Sure! What subject do you need help with?"

    elif "ai" in user_input:
        return "Artificial Intelligence is about making machines intelligent. You're already working on it! 😎"

    elif "python" in user_input:
        return "Python is a powerful and beginner-friendly programming language used in AI, web, and more!"

    # Time & Date
    elif "time" in user_input:
        return datetime.datetime.now().strftime("Current time is %H:%M:%S")

    elif "date" in user_input:
        return datetime.datetime.now().strftime("Today's date is %Y-%m-%d")

    # Weather (dummy response)
    elif "weather" in user_input:
        return "I can't access live weather, but I hope it's a nice day where you are! ☀️"

    # Fun / Jokes
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to the doctor? Because it caught a virus! 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
            "Why was the computer cold? It forgot to close its Windows! 😆"
        ]
        return random.choice(jokes)

    # Creator
    elif "who created you" in user_input:
        return "I was created by a student as part of an AI project! 🚀"

    # Capabilities
    elif "what can you do" in user_input:
        return "I can chat, answer questions, tell jokes, and help with basic topics!"

    # Thank you
    elif "thank" in user_input:
        return "You're welcome! 😊"

    # Default fallback
    else:
        return random.choice([
            "Hmm... I didn't understand that.",
            "Can you rephrase that?",
            "Interesting... tell me more!",
            "I'm still learning. Try asking something else 😊"
        ])

# Send message function
def send_message():
    user_text = entry_box.get()
    if user_text.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_text + "\n")

    response = chatbot_response(user_text)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)

    if user_text.lower() in ["exit", "bye", "quit"]:
        window.after(1000, window.destroy)

# GUI setup
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("500x600")
window.resizable(False, False)

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
chat_area.place(x=10, y=10, width=480, height=450)

# Entry box
entry_box = tk.Entry(window, font=("Arial", 14))
entry_box.place(x=10, y=470, width=370, height=40)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.place(x=390, y=470, width=100, height=40)

# Run app
window.mainloop()