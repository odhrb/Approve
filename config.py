import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

MONGO_URI = os.environ.get("MONGO_URI")
ADMIN_IDS = list(map(int, os.environ.get("ADMIN_IDS", "").split()))
START_PIC = os.environ.get("START_PIC", "")
APPROVAL_NOTE = os.environ.get("APPROVAL_NOTE", "You have been approved!")
