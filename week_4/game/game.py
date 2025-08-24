import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break

    except ValueError:
        continue

while True:
    try:
        correct = random.randint(1, level)
        guess = input("Guess: ")

        if guess > 0:

            if guess < correct:
                print("Too small!")
            elif guess > correct:
                print("Too Large!")
            elif guess == correct:
                print("Just right!")
                break
    except ValueError:
        continue