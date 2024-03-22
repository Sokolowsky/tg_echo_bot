import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6823518119:AAE4u7gj684utCAtHKxT_Agi6pnhTLQOnw4'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    print(updates)
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo=https://prnt.sc/1MzUIJ37qElw&caption=это моя тетя')
            requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo=https://prnt.sc/N2cFuRt7lnOu&caption=это моя тетя')

    time.sleep(1)
    counter += 1