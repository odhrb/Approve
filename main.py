from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import start, approve  # noqa

app = Client("auto_approve_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()# main bot logic
