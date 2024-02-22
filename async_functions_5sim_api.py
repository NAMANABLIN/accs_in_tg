import requests
from time import sleep
from pprint import pprint
import json
from config import SIM_TOKEN, OLD_SIM_TOKEN
import aiohttp

DOMAIN = '5sim.biz'


def reformat(response):
    return json.loads(response)


async def get_balance():
    headers = {
        'Authorization': 'Bearer ' + SIM_TOKEN,
        'Accept': 'application/json',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://{DOMAIN}/v1/user/profile', headers=headers) as response:
            return str(reformat(await response.text())['balance'])


async def get_number(country1: str, operator1: str, product1: str):
    headers = {
        'Authorization': 'Bearer ' + SIM_TOKEN,
        'Accept': 'application/json',
    }
    response = await aiohttp.get(f'https://{DOMAIN}/v1/user/buy/hosting/{country1}/{operator1}/{product1}',
                                 headers=headers)
    if response.status_code != 200:
        return "Ошибочка " + str(response.status_code) + response.content.decode('utf-8')
    else:
        return reformat(response)


async def old_get_number():
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

    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api1.{DOMAIN}/stubs/handler_api.php', params=params) as response:
            return str(await response.text())


async def get_sms(id: str):
    headers = {
        'Authorization': 'Bearer ' + SIM_TOKEN,
        'Accept': 'application/json',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://{DOMAIN}/v1/user/check/' + id, headers=headers) as response:
            return str(await response.text())


async def get_cost(country1: str, product1: str):
    headers = {
        'Accept': 'application/json',
    }

    params = (
        ('country', country1),
        ('product', product1),
    )

    response = await aiohttp.get(f'https://{DOMAIN}/v1/guest/prices', headers=headers, params=params)
    return reformat(response)
