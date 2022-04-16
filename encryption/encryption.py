import os
import pickle
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
key_url = os.path.join(BASE_DIR, 'key.key')


def generate_key():
    '''
    This function generates a key for encryption and decryption
    '''
    key = Fernet.generate_key()

    with open(key_url, 'wb') as key_file:
        pickle.dump(key, key_file)


def encrypt(data, depth=0):
    '''
    Encrypts the given parameter
    Parameters:
            data (str) or (dict): Data for encryption
            depth (int): Decides the depth of encryption
    Returns:
            data (str): Encrypted data
    '''
    if os.path.exists(key_url):
        with open(key_url, 'rb') as key_file:
            key = pickle.load(key_file)
    else:
        generate_key()

    fernet = Fernet(key)
    if depth == 0:
        data = str(data).encode('utf-8')
        data = fernet.encrypt(data).decode('utf-8')
    else:
        for item in data:
            for key, value in item.items():
                value = str(value).encode('utf-8')
                value = fernet.encrypt(value).decode('utf-8')
                item.update({key: value})

    return data


def decrypt(data, depth):
    '''
    Decrypts the given parameter
    Parameters:
            data (str) or (dict): Data for decryption
            depth (int): Decides the depth of encryption
    Returns:
            data (str): Decrypted data
    '''
    if os.path.exists(key_url):
        with open(key_url, 'rb') as key_file:
            key = pickle.load(key_file)
    else: 
        generate_key()

    fernet = Fernet(key)
    if depth == 0:
        data = str(data).encode('utf-8')
        data = fernet.decrypt(data).decode('utf-8')
    else:
        for item in data:
            for key, value in item.items():
                value = str(value).encode('utf-8')
                value = fernet.decrypt(value).decode('utf-8')
                item.update({key: value})

    return data
