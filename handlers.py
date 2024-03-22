from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from async_functions_5sim_api import (get_number, cancel_num, get_balance, finish_num,
                                      old_get_number, get_sms)
from keyboards import get_keyb
from config import data

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("get_number"))
async def get_number_handler(msg: Message, command: CommandObject):  # country, operator, product
    ans = (await old_get_number()).split(':')
    await msg.answer(f"ID заказа: `{ans[1]}`\nПолученный номер: +{ans[2]}", parse_mode='MARKDOWN',
                     reply_markup=get_keyb(ans[1], ["/get_sms", "/cancel", "/finish"]))


@router.message(Command("get_sms"))
async def get_number_handler(msg: Message, command: CommandObject):  # country, operator, product
    msg_text = command.text.split()
    ans = await get_sms(msg_text[1])
    if len(ans['sms']):
        await msg.answer(ans['sms'][0]["code"])
    else:
        await msg.answer('Сообщений пока нет')
    await msg.answer(ans['sms'])


@router.callback_query(F.data.startswith("get_sms "))
async def finish_number_callback(callback: types.CallbackQuery):
    msg_text = callback.data.split()
    ans = await get_sms(msg_text[1])
    if len(ans['sms']):
        await callback.answer(ans['sms'][0]["code"])
    else:
        await callback.answer('Сообщений пока нет')
    await callback.answer(ans['sms'])


@router.message(Command("finish"))
async def finish_number_handler(msg: Message, command: CommandObject):  # country, operator, product
    msg_text = command.text.split()
    status = await finish_num(msg_text[1])
    if status == 200:
        await msg.answer('Заказ завершён')
    else:
        print(status)
        await msg.answer('Какие-то проблемы, заказ не завершён')


@router.callback_query(F.data.startswith("finish "))
async def finish_number_callback(callback: types.CallbackQuery):
    msg_text = callback.data.split()
    status = await finish_num(msg_text[1])
    if status == 200:
        await callback.answer('Заказ завершён')
    else:
        await callback.answer('Какие-то проблемы, заказ не завершён')


@router.message(Command("cancel"))
async def cancel_number_handler(msg: Message, command: CommandObject):  # country, operator, product
    msg_text = command.text.split()
    status = await cancel_num(msg_text[1])
    print(status)
    if status == 200:
        await msg.answer('Заказ отменён')
    else:
        await msg.answer('Какие-то проблемы, заказ не отменён, скорее всего он создан не давно')


@router.callback_query(F.data.startswith("cancel "))
async def cancle_number_callback(callback: types.CallbackQuery):
    msg_text = callback.data.split()
    status = await cancel_num(msg_text[1])
    if status == 200:
        await callback.answer('Заказ отменён')
    else:
        await callback.answer('Какие-то проблемы, заказ не отменён, скорее всего он создан не давно')
