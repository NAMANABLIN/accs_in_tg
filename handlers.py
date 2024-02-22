from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from async_functions_5sim_api import get_number, get_balance, reformat, old_get_number, get_sms

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("get_number"))
async def get_number_handler(msg: Message, command: CommandObject):  # country, operator, product
    ans = (await old_get_number()).split(':')
    await msg.answer(f"ID заказа: {ans[1]}\nПолученный номер: +{ans[2]}")


@router.message(Command("get_sms"))
async def get_number_handler(msg: Message, command: CommandObject):  # country, operator, product
    id = command.text.split()
    ans = await get_sms(id[1])
    await msg.answer(ans)


@router.message(Command("get_balance"))
async def get_number_handler(msg: Message):
    ans = await get_balance()
    await msg.answer(ans)
