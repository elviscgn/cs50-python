"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    forbidden = ['.', "?", ","]
    length = len(s)
    reverse_s = s[::-1]
    s = s.strip()
    has_number = False

    for char in s:
        if char in forbidden:
            return False


    # check if our number plate has a number so
    # we can apply that logic of checking the last 3 characters for int
    for char in s:
        if char.isdigit():
            has_number = True
            break

    if not s[:2].isalpha():
        # print("failed first 2 alpha")
        return False

    if s in forbidden:
        # print("failed forbiden")
        return False

    if len(s) > 6 or len(s) < 2:
        # print("failed len")
        return False

    if has_number:
        if not progressive_number(s[::-1]):
            # print("failed last not digit")
            return False



    return True

def progressive_number(s):
    """
    Check if a string is progressively numbers
    only accepts strings with numbers
    eg "123Bar" returns true
    but "123bar3" returns false
    """
    numbers = []
    closed = False
    counter = 0
    for char in s:
        if char.isdigit():
            numbers.append(char)
            counter += 1
            if closed:
                return False
        if char.isalpha():
            closed = True


    if numbers[-1] == '0':
        return False

    if counter >= 1:
        return True

    return True


main()