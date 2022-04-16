import os, pickle
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
key_url = os.path.join(BASE_DIR, 'key.key')

def generate_key():
    
    key = Fernet.generate_key() 

    with open(key_url, 'wb') as key_file:
        pickle.dump(key, key_file)

def encrypt(data, depth=0):
    
    if os.path.exists(key_url):
        with open(key_url, 'rb') as key_file:
            key = pickle.load(key_file)
    else: generate_key()

    fernet = Fernet(key)
    if depth == 0:
        data = str(data).encode('utf-8')
        data = fernet.encrypt(data).decode('utf-8')
    else:
        for item in data:
            for key, value in item.items():
                value = str(value).encode('utf-8')
                value = fernet.encrypt(value).decode('utf-8')
                item.update({ key : value })

    return data

def decrypt(data, depth):
    
    if os.path.exists(key_url):
        with open(key_url, 'rb') as key_file:
            key = pickle.load(key_file)
    else: generate_key()

    fernet = Fernet(key)
    if depth == 0:
        data = str(data).encode('utf-8')
        data = fernet.decrypt(data).decode('utf-8')
    else:
        for item in data:
            for key, value in item.items():
                value = str(value).encode('utf-8')
                value = fernet.decrypt(value).decode('utf-8')
                item.update({ key : value })

    return data