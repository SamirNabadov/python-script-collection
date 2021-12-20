def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True


print(isPhoneNumber('415-554-2242'))

print()


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print('Done')

#######################################

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mp = phoneNumRegex.search('My number is 077-221-1755')
print('Phone number found: ' + mp.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mp = phoneNumRegex.search('My number is 077-221-1755')
print(mp.group(1))
print(mp.group(2))
print(mp.group(0))

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mp = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mp.group(1))
print(mp.group(2))
print(mp.group(0))

print()

heroRegex = re.compile(r'Batman|Tina Fey')
mo = heroRegex.search('Batman and Tina Fey.')
print(mo.group())
