from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardBuilder
from database.user_setter import set_user

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await set_user(message.from_user.id)
    await message.answer(f"Hello {message.from_user.full_name}, it's me Tasker bot!")


@router.message()
async def get_message_to_button(message: types.Message):
    some_tasks = ["task number one", "task number two", "task number three"]
    keyboard = InlineKeyboardBuilder()
    for index, task in enumerate(some_tasks):
        keyboard.add(InlineKeyboardButton(text=task, callback_data=f"task_{index}"))
    await message.answer(
        text="Press to completed task or write to create a new one",
        reply_markup=keyboard.adjust(1).as_markup()
    )
