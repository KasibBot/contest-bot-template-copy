from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# القائمة الرئيسية
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⭐ نقاطي"), KeyboardButton(text="🎟️ بطاقات السحب")],
        [KeyboardButton(text="📋 المهام"), KeyboardButton(text="🎁 المسابقات")],
        [KeyboardButton(text="🏆 المتصدرون"), KeyboardButton(text="👥 دعوة صديق")],
        [KeyboardButton(text="📜 القوانين"), KeyboardButton(text="📞 الدعم")],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "💰 مرحبًا بك في Kasib\n\n"
        "اكسب النقاط، شارك في المسابقات، واربح الجوائز!\n\n"
        "اختر أحد الخيارات من القائمة 👇",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "⭐ نقاطي")
async def my_points(message: Message):
    await message.answer("⭐ نقاطك الحالية: 0")

@dp.message(F.text == "🎟️ بطاقات السحب")
async def tickets(message: Message):
    await message.answer("🎟️ لا تملك أي بطاقة سحب حتى الآن.")

@dp.message(F.text == "📋 المهام")
async def tasks(message: Message):
    await message.answer("📋 لا توجد مهام متاحة حاليًا.")

@dp.message(F.text == "🎁 المسابقات")
async def contests(message: Message):
    await message.answer("🎁 لا توجد مسابقات نشطة حاليًا.")

@dp.message(F.text == "🏆 المتصدرون")
async def leaderboard(message: Message):
    await message.answer("🏆 سيتم عرض قائمة المتصدرين هنا.")

@dp.message(F.text == "👥 دعوة صديق")
async def invite(message: Message):
    await message.answer("👥 رابط الدعوة الخاص بك سيظهر هنا.")

@dp.message(F.text == "📜 القوانين")
async def rules(message: Message):
    await message.answer("📜 قوانين استخدام Kasib ستضاف هنا.")

@dp.message(F.text == "📞 الدعم")
async def support(message: Message):
    await message.answer("📞 تواصل مع الدعم قريبًا.")

# Web Server لـ Render
async def health(request):
    return web.Response(text="Kasib Bot is running!")

async def run_web_server():
    app = web.Application()
    app.router.add_get("/", health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 10000)))
    await site.start()

async def main():
    await run_web_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
