# config.py
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8793337867:AAHLysIOzj4Dj8T4QQfHk06rSx6l83wkMY8")
OWNER_ID = int(os.environ.get("OWNER_ID", 8950729666))
DEV_NAME = "RIP AMIN"
DEV_USER = "amin9384n"

KEY_PREFIX = "Amin-KEY"
MAX_DEVICES_DEFAULT = 5

KEYS_FILE = "keys.json"
USERS_FILE = "users.json"
BOT_STATUS_FILE = "bot_status.json"

LANG_EN = "en"
LANG_AR = "ar"

FLASK_PORT = int(os.environ.get("PORT", 5000))
FALLBACK_URL = "http://localhost:5000"