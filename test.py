import requests
import json
from encryption.encryption import decrypt

BASE_URL = 'http://127.0.0.1:5000/'


def create():
    '''
    This function that demonstartes the usage of create API endpoint
    '''

    url = BASE_URL+'create_task'
    payload = {
                'content': 'A newerer task',
                'username': 'root',
                'password': 'root'
            }

    response = requests.request('POST', url, data=payload)

    data = json.loads(response.text)
    print('ENCRYPTED:', data.get('message'))
    print('DECRYPTED:', decrypt(data=data.get('message'), depth=0))


def update():
    '''
    This function that demonstartes the usage of update API endpoint
    '''

    url = BASE_URL+'update_task'
    payload = {
            'username': 'root',
            'password': 'root',
            'task': '1',
            'content': 'this is new content'
            }

    response = requests.request('POST', url, data=payload)

    data = json.loads(response.text)
    print('ENCRYPTED:', data.get('message'))
    print('DECRYPTED:', decrypt(data=data.get('message'), depth=0))


def read():
    '''
    This function that demonstartes the usage of read API endpoint
    '''

    url = BASE_URL+'read_task'
    payload = {
        'username': 'root',
        'password': 'root'
        }

    response = requests.request('POST', url, data=payload)

    data = json.loads(response.text)
    print('ENCRYPTED:', data.get('message'))
    if isinstance(data.get('message'), str):
        depth = 0
    else:
        depth = 1
    print('DECRYPTED:', decrypt(data=data.get('message'), depth=depth))


def delete():
    '''
    This function that demonstartes the usage of delete API endpoint
    '''

    url = BASE_URL+'delete_task'
    payload = {
            'username': 'root',
            'password': 'root',
            'task': '1'
            }

    response = requests.request('POST', url, data=payload)

    data = json.loads(response.text)
    print('ENCRYPTED:', data.get('message'))
    print('DECRYPTED:', decrypt(data=data.get('message'), depth=0))

if __name__ == '__main__':
    create()
    update()
    read()
    delete()
