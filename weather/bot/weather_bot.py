from os import getenv
from dotenv import load_dotenv
from aiogram import Dispatcher,Bot,types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from . import weather_resp



load_dotenv()



dp = Dispatcher()
bot = Bot(token=getenv("BOT_TOKEN"))



class Weather(StatesGroup):
    temperature=State()



@dp.message(Command("start"))
async def washing_clothes(message:Message,state:FSMContext):
    await message.answer("Welcome to weather bot\nEnter your temperature")
    await state.set_state(Weather.temperature)



@dp.message(Weather.temperature)
async def temperature(message:Message):
    temperature = message.text
    resp = await weather_resp(temperature)
    await message.answer(resp)



