import random

name = input("What is your name? ").strip()
question = input("What is your question for the Magic 8-Ball? ").strip()

answers = [
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "I very much think so",
]

if not question:
    print("You didn't enter a question :(")
else:
    answer = random.choice(answers)
    if not name:
        print(f"Question: {question}")
    else:
        print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
