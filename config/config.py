import os

TOKEN = os.getenv("BOT_TOKEN")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
GROUP_ID = int(os.getenv("GROUP_ID", 0))
SUPPORT_CHAT_ID = int(os.getenv("SUPPORT_CHAT_ID", 0))
RESULTS_GROUP_ID = int(os.getenv("RESULTS_GROUP_ID", 0))
