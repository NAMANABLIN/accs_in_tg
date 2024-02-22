import requests
from time import sleep
from pprint import pprint
import json
from config import SIM_TOKEN, OLD_SIM_TOKEN

DOMAIN = '5sim.biz'


def reformat(response):
    return json.loads(response.content.decode('utf-8'))


def get_balance():
    headers = {
        'Authorization': 'Bearer ' + SIM_TOKEN,
        'Accept': 'application/json',
    }

    response = requests.get(f'https://{DOMAIN}/v1/user/profile', headers=headers)
    return response.content.decode('utf-8')


def get_number(country1: str, operator1: str, product1: str):
    headers = {
        'Authorization': 'Bearer ' + SIM_TOKEN,
        'Accept': 'application/json',
    }
    response = requests.get(f'https://{DOMAIN}/v1/user/buy/hosting/{country1}/{operator1}/{product1}',
                            headers=headers)
    if response.status_code != 200:
        return "Ошибочка " + str(response.status_code) + response.content.decode('utf-8')
    else:
        return reformat(response)


def old_get_number():
    country = 15
    service = 'bz'
    operator = 'virtual32'

    params = (
        ('api_key', OLD_SIM_TOKEN),
        ('country', country),
        ('action', 'getNumber'),
        ('service', service),
        ('operator', operator)
    )

    response = requests.get(f'http://api1.{DOMAIN}/stubs/handler_api.php', params=params)
    return response.content.decode('utf-8')


def get_cost(country1: str, product1: str):
    headers = {
        'Accept': 'application/json',
    }

    params = (
        ('country', country1),
        ('product', product1),
    )

    response = requests.get(f'https://{DOMAIN}/v1/guest/prices', headers=headers, params=params)
    return reformat(response)


if __name__ == '__main__':
    country = 'poland'
    operator = 'virtual34'
    product = 'blizzard'

    # print(get_balance())

    # print(get_number(country, operator, product))
    # pprint(get_cost(country, product))
    print(old_get_number())
