from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from callbacksfactory import NumbersCallbackFactory


def get_keyb(id: str, commands: list):
    builder = InlineKeyboardBuilder()
    [builder.row(InlineKeyboardButton(text=x + ' ' + id, callback_data=x + '_' + id)) for x in commands]
    return builder.as_markup()
