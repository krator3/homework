import os

from aiogram import types
from dotenv import load_dotenv

load_dotenv()

ADMINS = (381762408,)  # Тут ваш id

TOKEN = os.getenv('TOKEN')
if not TOKEN:
    exit('Error: no token provided')

COMMANDS = [
    types.BotCommand('start', 'Стартуем!'),
    types.BotCommand('fetchone', 'Получение одной записи БД'),
    types.BotCommand('fetchall', 'Получение всех ваших записей БД'),
    types.BotCommand('ban', 'Забанить'),
]
