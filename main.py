import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, Chat
# import aiogram.utils.markdown as text_decorate

with open("TOKEN", "r") as f:
    TOKEN = f.read()


dp = Dispatcher()
log = print


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


@dp.message(Command("test"))
async def command_test_handler(message: Message) -> None:
    s = []
    s.append(message.chat.id)
    s.append(message.message_id)
    await print_bot(message, s)
    for i in range(10):
        message_new = await bot.copy_message(
            from_chat_id=message.chat.id,
            chat_id=message.chat.id,
            message_id=10
        )
        print(message_new)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    s = []
    s.append(f"Привіт, <b><i>{message.from_user.full_name}</i></b>!")
    s.append(f"Напиши /help щоб дізнатись, що я роблю")
    await message.answer("\n".join(s))


@dp.message(Command("help"))
async def command_help_handelr(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    s = []
    s.append(f"Я створюю готове телеграм повідомлення про оголошення з OLX")
    s.append(f"Скинь мені посилання на оголошення і я спробую, щось зробити")
    await message.answer("\n".join(s))


@dp.message()
async def echo_response(message: Message) -> None:
    try:
        await message.send_copy(message.chat.id)
    except:
        await message.answer("На жаль я не можу цього відправити")


async def print_bot(message: Message, s: list) -> None:
    await message.answer("\n".join([str(c) for c in s]))


if __name__ == "__main__":
    asyncio.run(main())
