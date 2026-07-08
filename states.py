from aiogram.fsm.state import StatesGroup, State


class TaskState(StatesGroup):
    waiting_for_proof = State()
