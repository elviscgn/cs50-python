message = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if message.strip() == "42" or message.lower() == "forty two" or message.lower() == "forty-two":
    print("Yes")
else:
    print("No")