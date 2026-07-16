from aiogram.fsm.state import State, StatesGroup

class SupportState(StatesGroup):
    waiting_for_message = State()

class ReplyState(StatesGroup):
    waiting_for_reply = State()

class TaskState(StatesGroup):
    waiting_for_proof = State()
    
class ContestState(StatesGroup):
    waiting_for_title = State()
    waiting_for_prize = State()
    waiting_for_winners = State()
