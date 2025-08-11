prompt = input("camelCase: ")

indexes = []
snake_case = ""
for i, char in enumerate(prompt):
    if char.isupper():
        indexes.append(i)

for i, char in enumerate(prompt):
    if i in indexes:
        snake_case += "_"
    snake_case += char.lower()


print("snake_case: ", snake_case)
