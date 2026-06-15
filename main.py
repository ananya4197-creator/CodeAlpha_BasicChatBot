def chatbot():
    print("=" * 40)
    print("      Welcome to Simple ChatBot")
    print("Type 'bye' to exit the chat")
    print("=" * 40)

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How about you?")
        elif user_input == "what is your name":
            print("Bot: My name is ChatBot.")
        elif user_input == "help":
            print("Bot: You can say hello, ask how are you, or type bye.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()