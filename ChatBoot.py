def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["hi", "hello"]:
            print("Chatbot: Hi there!")
        elif user_input in ["how are you"]:
            print("Chatbot: I'm fine, thank you!")
        elif user_input in ["bye", "exit"]:
            print("Chatbot: Goodbye! 👋")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
