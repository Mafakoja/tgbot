import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from .config import settings
from .database import SessionLocal, init_db
from .models import Message

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.token)
dp = Dispatcher(bot)

init_db()


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    await save_message(message.from_user.id, 'text', message.text)
    await message.reply("Ваше сообщение сохранено")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def handle_photo(message: types.Message):
    file_id = message.photo[-1].file_id
    await save_message(message.from_user.id, 'photo', file_id)
    await message.reply("Ваше фото сохранено")


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def handle_video(message: types.Message):
    file_id = message.video.file_id
    await save_message(message.from_user.id, 'video', file_id)
    await message.reply("Ваше видео сохранено")


async def save_message(user_id: int, msg_type: str, content: str):
    session = SessionLocal()
    try:
        msg = Message(user_id=user_id, message_type=msg_type, content=content)
        session.add(msg)
        session.commit()
    finally:
        session.close()


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
