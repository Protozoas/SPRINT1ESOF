def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False       
    if text[3] != 9:
        return False
    for i in range(4, 12):
        if not text[i].isdecimal():
            return False
    return True

print('012986584722 is a phone number?')
print(isPhoneNumber('012986584722'))
print('Roorona Zoro is a phone number?')
print(isPhoneNumber('Roorona Zoro'))
