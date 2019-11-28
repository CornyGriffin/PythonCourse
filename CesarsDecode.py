def cesarcode(ll, l_key):
    code = ord(ll)
    newCode = ord(ll) - l_key
    if ll in string.ascii_lowercase:
        if newCode < ord("a"):
            newCode = newCode + 26
    elif ll in string.ascii_uppercase:
        if newCode < ord("A"):
            newCode = newCode + 26
    else:
        newCode = code

    new_ll = chr(newCode)
    return new_ll


letters = "Vyyu dy wi mywsxq yx dro psbcd vsqrd yp dro pspdr nki, kd nkgx vyyu dy dro okcd."
key = int(input("Key>>")) # key = 10

for letter in letters:
    newLetter = cesarcode(letter, key)
    print(newLetter, end="", flush=True)
