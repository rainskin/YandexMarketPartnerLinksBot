from aiogram import types, F
from aiogram.filters import Command

import texts
from loader import bot, dp
from request import create_partner_url


@dp.message(Command('start'))
async def cmd_start(msg: types.Message):
    await msg.answer(texts.command_start)


@dp.message(F.text.startswith('https://market.yandex'))
async def create_link(msg: types.Message):
    url = create_partner_url(msg.text)
    await msg.answer(f'Твоя ссылка {url}')


@dp.message()
async def send_guide(msg: types.Message):
    await msg.answer(texts.guide)


dp.run_polling(bot)
