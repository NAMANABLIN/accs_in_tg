from typing import Optional
from aiogram.filters.callback_data import CallbackData


class NumbersCallbackFactory(CallbackData, prefix="fabsms"):
    action: str
    value: Optional[int] = None
