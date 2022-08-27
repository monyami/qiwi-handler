import requests, time, logging, json, math, sys
import config, variables


def get_balance(session: requests.Session()):
    response = session.get(variables.url_balance, headers=variables.headers_balance).text
    return (json.loads(response))['accounts'][0]['balance']['amount']


# Отправить средства p2p
def send_p2p(session: requests.Session(), sum: int):
    data_pay = {
        'id': str(int(time.time() * 1000)),
        'sum':{'amount':f'{sum}','currency':'643'},
        'paymentMethod':{'type':'Account','accountId':'643'},
        'comment':'',
        'fields':{'account': f'+{config.phone_receiver}'}
    }

    resp = session.post(variables.url_pay, headers=variables.headers_pay, json=data_pay)
    print(resp.text)
    return resp

if __name__ == '__main__':
    # Вывод лога
    logging.basicConfig(level=logging.INFO)
    logging.info(variables.msg_start)
    # Создание и настройка сессии
    session = requests.Session()
    session.proxies.update(config.proxies)
    # Проверка прокси
    if len(session.proxies) == 0:
        logging.warning(variables.msg_warning)
        sys.exit(0)
    
    while(True):
        try:
            balance = get_balance(session)
            # Проверка баланса
            if balance >= config.min_sum:
                # Учёт комисcии
                sum = int(math.floor(balance) * 0.98)
                if send_p2p(session, sum):
                    # Перевод выполнен
                    logging.info("\033[32m" + " Операция на сумму '" + str(sum) + "' RUB проведена успешно!" + "\033[0m")
                else:
                    # Перевод не выполнен
                    logging.warning(variables.msg_fail)
            time.sleep(10)
        # Завершение скрипта
        except KeyboardInterrupt:
            logging.info(variables.msg_stop)
            session.close()
            sys.exit(0)
