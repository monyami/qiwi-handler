import config
import time

# Константные данные
headers_balance = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {config.token}'
}

headers_pay = {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Authorization': f'Bearer {config.token}'
}

url_balance = f'https://edge.qiwi.com/funding-sources/v2/persons/{config.phone}/accounts'

url_pay = 'https://edge.qiwi.com/sinap/api/v2/terms/99/payments'

msg_start = "\033[32m" + " Скрипт запущен!" + "\033[0m"

msg_warning = '\033[91m' + ' Прокси не подключен! Скрипт остановлен!' + '\033[0m'

msg_stop = "\033[32m" + " Скрипт завершён корректно!" + "\033[0m"

msg_fail = '\033[91m' + ' Не удалось перевести средства!' + '\033[0m'