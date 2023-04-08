import sqlite3

from aiogram import types

from loader import dp


@dp.message_handler(commands=['ban'])
async def member_off(msg: types.Message):
    arg = msg.get_args().split(':')  # /ban 381762408:по приколу 2
    if len(arg) == 2:
        user_id_ban = arg[0]
        timestamp = msg.date.timestamp()
        reason = arg[1]

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute(
                """
                insert into block_list(user_id, timestamp, reason) VALUES (?,?,?);
                """,
                (
                    user_id_ban,
                    timestamp,
                    reason,
                )
            )
            conn.commit()
        await msg.answer('Пользователь добавлен в бан!')
