message = input()
final_message = ""
for i, m in enumerate(message.split()):

    if i+1 < len(message.split()):
        final_message += m + "..."
    else:
        final_message += m

print(final_message)