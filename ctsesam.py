#!/usr/bin/env python3
"""
    ctsesam.py


    Siehe c't wissen 'Python-Projekte'

    Programmieren lernen mit c't SESAM
    1234

"""
from hashlib import pbkdf2_hmac

lower_case_letters = list('abcdefghijklmnopqrstuvwxyz')
upper_case_letters = list('ABCDEFGHJKLMNPQRTUVWXYZ')
numbers = list('0123456789')
special_characters = list('#!"$$%&/()[]{}=-_+*<;:.')
password_characters = lower_case_letters + upper_case_letters + numbers +\
                      special_characters
SALT = 'pepper'

def convert_bytes_to_password(hashed_bytes, length):
    """

    """
    number = int.from_bytes(hashed_bytes, byteorder='big')
    password = ''
    while number > 0 and len(password) < length:
        password = password + password_characters[number %
                                                  len(password_characters)]
        number = number // len(password_characters)
    return password

print("This is ctSesam")

MASTER_PASSWORD = input('Masterpasswort: ')
DOMAIN = input('Domain: ')
while len(DOMAIN) < 1:
    print('Bitte eine Domain eingeben.')
    DOMAIN = input('Domain: ')

hash_string = DOMAIN + MASTER_PASSWORD
hashed_bytes = pbkdf2_hmac('sha512',
                           hash_string.encode('utf-8'),
                           SALT.encode('utf-8'),
                           4096)

print('Password: ' + convert_bytes_to_password(hashed_bytes, 10))
