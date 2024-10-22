from multiprocessing import pool
from requests import get

DOMAIN = ''#soon

def send_request(val):
    while True:
        response = get(f'https://{DOMAIN}')
        data = response.json()
        print('Sent Request')
        print(data)