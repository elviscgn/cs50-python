message = input("Greeting: ")

if "hello" in message.lower().strip():
    print("$0")
elif "how" in message.lower().strip():
    print("$20")
elif "what's" in message.lower().strip():
    print("$100")