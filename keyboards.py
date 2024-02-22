from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callbacksfactory import NumbersCallbackFactory

def get_keyb(id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Проверить смс", callback_data=NumbersCallbackFactory(action="get_sms", value=1))]])
