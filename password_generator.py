#!/usr/bin/python

import random
import string
import pyperclip
import sys

""" 
    @author: Emmanuel Hernandez - @snipa.v1

    This script will generate a complex password offline through terminal and
    copy the password to clipboard

"""

def main():
    special_chars = "!@#$%^&*()"
    word_length = 0

    is_long = False
    while not is_long:
        length = int(raw_input("[.] What length of password would you like: \n    (minimum = 12) \n\n> "))
        if length >= 12:
            is_long == True
            word_length = length
            break
        else:
            print("\n[!] Password must be at least 12 characters long!\n")

    def generate_password(l):
        return "".join(
            random.choice(string.ascii_lowercase + string.digits + special_chars) for
            _ in range(l))

    done = False
    yes_no = ""

    print("\n[*] Press 'e' or type 'exit' to exit")

    while not done or yes_no != 'e':

        password = generate_password(word_length)

        yes_no = raw_input("\n[.] Would you like to use: '{}' (y or n)?\n\n> ".format(password))

        yes_no = yes_no.lower()

        if yes_no == "e" or yes_no == 'exit':
            print("\n[%] Exiting...")
            sys.exit()
        if yes_no == 'y' or yes_no == 'yes':
            pyperclip.copy(password)
            print("\n[%] '{}' copied to clipboard successfully!\n".format(password))
            done = True
            break
        elif yes_no == 'n' or yes_no == 'no':
            continue
        else:
            print("\n[!] Please enter: 'y' or 'n'")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[!] KeyboardInterrupt Detected.')
        print('[%] Exiting...')
        exit(0)
