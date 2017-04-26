import re

message = 'Call me at 415-555-1011 or 212-555-9999 tomorrow'
phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
cap = phoneNum.findall(message)
print('Ok, I\'ll call you on one of your both numbers: ' + str(cap))
