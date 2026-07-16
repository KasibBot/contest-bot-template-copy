import os

# ==========================
# Telegram
# ==========================

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

BOT_NAME = os.getenv("BOT_NAME", "Contest Bot")

# ==========================
# Supabase
# ==========================

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ==========================
# Groups
# ==========================

GROUP_ID = int(os.getenv("GROUP_ID", "0"))
SUPPORT_CHAT_ID = int(os.getenv("SUPPORT_CHAT_ID", "0"))
RESULTS_GROUP_ID = int(os.getenv("RESULTS_GROUP_ID", "0"))

# ==========================
# Rewards
# ==========================

REFERRAL_REWARD = int(os.getenv("REFERRAL_REWARD", "10"))
EXCHANGE_COST = int(os.getenv("EXCHANGE_COST", "1000"))
