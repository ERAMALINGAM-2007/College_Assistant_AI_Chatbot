from chatbot import ask

while True:

    question = input("You: ")

    if question == "exit":
        break

    answer = ask(question)

    print("\nAssistant:\n")
    print(answer)
    print()