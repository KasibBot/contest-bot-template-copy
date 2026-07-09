from aiogram.fsm.state import StatesGroup, State


class TaskState(StatesGroup):
    waiting_for_proof = State()


class AdminTaskState(StatesGroup):
    waiting_for_title = State()
    waiting_for_url = State()
    waiting_for_points = State()
