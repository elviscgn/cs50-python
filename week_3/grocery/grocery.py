
def compute_stack(stack):
    new_stack = dict()

    for s in stack:
        if new_stack.get(s):
            new_stack[s] += 1
        else:
            new_stack[s] = 1
    for k,v in sorted(new_stack.items()):
        print(f"{v} {k.upper()}")

stack = []

while True:
    try:
        item = input().lower()
        stack.append(item)

    except EOFError:
        compute_stack(stack)
        break