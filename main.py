from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from random import randint
import pickle
from tokenbot import TOKEN


class User:
    def __init__(self):
        self.potuzhnost = -1


bot = Bot(token=TOKEN)
dp = Dispatcher()
with open("users.pickle", "rb") as file:
    users = pickle.load(file)


def check_user(message: Message):
    global users
    if message.from_user.id not in users:
        users[message.from_user.id] = User()
        with open("users.pickle", "wb") as file:
            users = pickle.dump(users, file)


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await check_user(message)
    await message.reply("/get_potuzhnost - дізнатися свою потужність!")

@dp.message(Command(commands=["get_potuzhnost"]))
async def process_potuzhnost_command(message: Message):
    check_user(message)
    print(message.from_user.id)
    #if users[message.from_user.id].potuzhnost == -1:
    potuzhnost = randint(0, 100)
    users[message.from_user.id].potuzhnost = potuzhnost
    await message.reply(f"ваша потужність - {users[message.from_user.id].potuzhnost}%")




if __name__ == '__main__':
    dp.run_polling(bot)