import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor

def make_http_request(request_number, message, chat_id, bot_token):
    with requests.Session() as session:
        try:
            response = session.post(
                f'https://api.telegram.org/{bot_token}/sendMessage',
                params={
                    'parse_mode': 'markdown',
                    'chat_id': chat_id,
                    'text': message
                }
            )

            response_json = response.json()
            if 'result' in response_json and 'message_id' in response_json['result']:
                print(f"teks sukses bang msgid : {response_json['result']['message_id']}")
            else:
                print("request timeout bang")
        except Exception as e:
            print("request timeout bang")

# Membaca pesan dan chat id target dari file
with open("pesan.txt", "r") as pesan_file:
    message = pesan_file.read()

with open("target.txt", "r") as target_file:
    chat_id = target_file.read()

with open("token.txt", "r") as token_file:
    bot_token = token_file.read().strip()

num_threads = int(input("Masukkan jumlah thread yang ingin digunakan: "))

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    request_count = 0
    while True:
        request_count += 1
        executor.submit(make_http_request, request_count, message, chat_id, bot_token)
