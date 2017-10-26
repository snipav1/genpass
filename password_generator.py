#!/usr/bin/python

# Author: Emmanuel A. Hernandez <@snipa.v1>

import random
import string
import pyperclip
import sys

""" 
    @author: Emmanuel Hernandez

    This script will generate a complex password offline through terminal and
    copy the password to clipboard

"""

SPECIAL_CHARS = "!@#$%^&*()"
word_length = 0

is_long = False
while not is_long:
    length = int(raw_input("[.] What length of password would you like: \n> "))
    if length >= 12:
        is_long == True
        word_length = length
        break
    else:
        print("[!] Password must be at least 12 characters long!\n")


def generate_password(l):
    return "".join(
        random.choice(string.ascii_lowercase + string.digits + SPECIAL_CHARS) for
        _ in range(l))

done = False
yes_no = ""

print("[.] Press 'e' to exit")

while not done or yes_no != 'e':

    password = generate_password(word_length)

    yes_no = raw_input("[.] Would you like to use: '{}' (y or n)?\n> ".format(password))

    if yes_no == "e":
        sys.exit()
    elif yes_no.lower() == 'y' or yes_no.lower() == 'yes':
        pyperclip.copy(password)
        print("[.] '{}' copied to clipboard successfully!\n".format(password))
        done = True
        break
