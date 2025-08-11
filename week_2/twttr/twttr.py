prompt = input("Input: ")
clean = ""
vowels = "aeiou"

for char in prompt:
    if char.lower() not in vowels:
        clean += char

print("Output:", clean)
