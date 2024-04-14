from aiogram.dispatcher.filters.state import State, StatesGroup

class StateRegistration(StatesGroup):
    name = State()
    password = State()