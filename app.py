import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram import Router
from aiogram.types import FSInputFile

BOT_TOKEN = "6782067539:AAGBEbm95qipwVRs1AxkjgDZ7YzOV6gRynI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

@dp.message(Command("start"))
async def send_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="GitHub", 
                    web_app=WebAppInfo(url="https://github.com/ermekovtariel/")
                ),
                InlineKeyboardButton(
                    text="CV", 
                    web_app=WebAppInfo(url="https://www.canva.com/design/DAGawcSI9D8/kVWPBZ0dbghtIh6odIvpNQ/edit?utm_content=DAGawcSI9D8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
                )
            ],
            [
                InlineKeyboardButton(
                    text="Download CV", 
                    callback_data="download_cv"
                ),
                InlineKeyboardButton(
                    text="My Taplink", 
                    web_app=WebAppInfo(url="https://etariel.taplink.ws")
                )
                
            ]
        ]
    )

    photo_caption = "Hello! 👋\n" + "I'm Ermekov Tariel's personal bot.\n\n" + "He is an experienced React Frontend Developer with deep knowledge in React development.js, Redux, TypeScript, and other technologies. 🛠️\n\n" + "A little bit about him:\n" + "🌍 He has been working in IT since 2020.\n" + "💻 Participated in the development of several companies such as Kundoluk, Level Up Star, and WildBox.\n" + "🎨 Uses tools such as Vite, Figma, Firebase, and Axios.\n\n" + "To see his pet-projects, click below!"

    photo_url = 'https://avatars.githubusercontent.com/u/62035728?v=4'
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=photo_caption, reply_markup=keyboard)


@router.callback_query(lambda c: c.data == "download_cv")
async def send_cv(callback_query: types.CallbackQuery):
    file_path = os.getcwd() + '/Ermekov_Tariel_CV.pdf'  # Убедитесь, что путь правильный
    try:
        # Создаем объект InputFile, передавая путь к файлу
        document = FSInputFile(file_path)

        # Отправляем документ
        await bot.send_document(callback_query.from_user.id, document)
        await callback_query.answer('Sending CV...')
    except Exception as e:
        print(e)
        await callback_query.answer(f"Error: {e}")
        
async def main():
    dp.include_router(router)  # Подключаем маршрутизатор
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
