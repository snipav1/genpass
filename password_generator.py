#!/usr/bin/python3

import random
import string
import pyperclip
import sys

"""
@author: Emmanuel Hernandez - @snipa.v1

    This script will generate a complex password offline through terminal and
    copy the password to clipboard

"""
BANNER = """
-------------------------------------------------------
______ _______ __   _  _____  _______ _______ _______
|  ____ |______ | \  | |_____] |_____| |______ |______
|_____| |______ |  \_| |       |     | ______| ______|

-------------------------------------------------------
"""
print(BANNER)

SPECIAL_CHARS = "!@#$%^&*()"


class Color:
    OKBLUE = '\033[94m'
    ENDC = '\033[0m'


def generate_password(length):
    return "".join(
        random.
        choice(string.ascii_lowercase + string.digits + SPECIAL_CHARS) for
        _ in range(length))


def main():
    word_length = 0
    is_long = False
    while not is_long:
        length = int(
            input("[.] What length of password would you like: \
                  \n    (minimum = 12) \n\n> "))
        if length >= 12:
            word_length = length
            is_long = True
            break
        else:
            print("\n[!] Password must be at least 12 characters long!\n")

    yes_no = ""
    print("[.] Word length is: {}".format(str(word_length)))

    print("\n[*] Press 'e' or type 'exit' to exit")

    while yes_no != 'e':

        password = generate_password(word_length)

        yes_no = input(
            f"\n[.] Would you like to use: '{Color.OKBLUE}{password}{Color.ENDC}' (y or n)?\n\n> ")

        yes_no = yes_no.lower()

        if yes_no == "e" or yes_no == 'exit':
            print("\n[%] Exiting...")
            sys.exit()
        if yes_no == 'y' or yes_no == 'yes':
            pyperclip.copy(password)
            print(
                f"\n[%] '{Color.OKBLUE}{password}{Color.ENDC}' copied to clipboard successfully!\n")
            sys.exit()
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
