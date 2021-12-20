#!/usr/bin/python3.8

import string
import getpass

def passwordValidator():
    """
    Validates passwords to match specific rules
    : return: str
    """
    # display rules that a password must conform to
    print('\nYour password should: ')
    print('\t- Have a minimum length of 6;')
    print('\t- Have a maximum length of 12;')
    print('\t- Contain at least an uppercase letter or a lowercase letter')
    print('\t- Contain at least a number;')
    print('\t- Contain at least a special character (such as @,+,£,$,%,*^,etc);')
    print('\t- Not contain space(s).')
    # get user's password
    userPassword = getpass.getpass('\nEnter a valid password: ').strip()
   # check if user's password conforms 
   # to the rules above
    if not(6 <= len(userPassword) <= 12):
        message = "Invalid Password... Your password should have a minimum"
        message += "Length of 6 and a minimum length f 12"
        return message
    if ' ' in userPassword:
       message = 'Invalid Password... Your password shouldn\'t contain space(s)'
       return message
    if not any(i in string.ascii_letters for i in userPassword):
       message = 'Invalid Password..your password should contain at least '
       message += 'an uppercase letter and a lowercase letter'
       return message
    if not any(i in string.digits for i in userPassword):
        message = 'Invalid Password..your password should contain at least a number'
        return message
    if not any(i in string.punctuation for i in userPassword): 
       message = 'Invalid Password..your password should contain at least a special character'
       return message
    else:
        return "Valid Password!"


def main():
    while True:
        choice = input("Do you want to check a password's strength (y/n) : ")
        if 'y' in choice.lower():
            my_password = passwordValidator()
            print(my_password)
        elif 'n' in choice.lower():
            print("Exiting...")
            break
        else:
            print("Invalid input... Please try again.")
        print()

if __name__ == '__main__':
    main()


