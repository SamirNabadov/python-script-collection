#!/usr/bin/python3.8
import subprocess
from datetime import datetime



def get_password_expiry_from_chage(account):
    try:
        chage = subprocess.Popen(('chage', '-l', account), shell=False, stdout=subprocess.PIPE, universal_newlines=True)
        grep = subprocess.Popen(('grep', 'Account expires'), shell=False, stdin=chage.stdout, stdout=subprocess.PIPE, universal_newlines=True)
        cut = subprocess.Popen('cut -d : -f2'.split(), shell=False,  stdin=grep.stdout, stdout=subprocess.PIPE, universal_newlines=True)
        output = cut.communicate()[0].strip()
        return output if output != 'never' else None
    except subprocess.CalledProcessError as e:
        return None

def is_going_to_expire(chage_date):
    BUFFER_DURATION = 60 # in days
    expiry_date = datetime.strptime(chage_date, '%b %d, %Y')
    today = datetime.now()
    return abs((expiry_date - today).days) <= BUFFER_DURATION

def main():
    accounts = ['ansible','root','nabadov']
    for account in accounts:
        # Get expiry date from chage program
        chage_date = get_password_expiry_from_chage(account)
        # Determine if password is going to expire for account
        if chage_date != None and is_going_to_expire(chage_date):
            print(account + ' is going to expire on ' + chage_date)


if __name__== "__main__":
    main()
