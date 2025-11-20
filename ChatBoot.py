import time
import random

# Predefined replies for Person B
responses = {
    "hello": ["Hi! How are you?", "Hello! Nice to meet you!"],
    "how are you": ["I'm good! What about you?", "Feeling great today!"],
    "what are you doing": ["Just chatting here!", "Relaxing and talking with you."],
    "bye": ["Goodbye!", "See you soon!"]
}

# Random filler replies
default_replies = [
    "Hmm, interesting!",
    "Tell me more.",
    "Oh really?",
    "That's nice!",
    "I see..."
]

def get_response(msg):
    msg = msg.lower()
    for key in responses:
        if key in msg:
            return random.choice(responses[key])
    return random.choice(default_replies)

def conversation():
    personA_lines = [
        "Hello!",
        "How are you?",
        "What are you doing?",
        "That sounds good!",
        "Bye"
    ]

    print("\n💬 Conversation Simulation Started:\n")

    for line in personA_lines:
        print("Person A:", line)
        time.sleep(1.2)

        reply = get_response(line)
        print("Person B:", reply)
        time.sleep(1.4)

        if "bye" in line.lower():
            print("\nConversation Ended.")
            break

conversation()
