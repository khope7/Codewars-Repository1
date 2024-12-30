def is_isogram(string):
    factcheck = 0
    check = []
    for char in string:
        char = char.lower()
        if char not in check:
            check.append(char.lower())
        elif char in check:
            factcheck = 1
    if factcheck == 0:
        return False
    if factcheck == 1:
        return True

is_isogram("Thisisatest")