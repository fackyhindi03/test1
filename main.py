# main.py
import os
import logging
from telethon import TelegramClient
from config import API_ID, API_HASH
from handlers import register_handlers

# Load environment variables (API_ID, API_HASH, BOT_TOKEN, etc.)
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN must be set in your .env")

logging.basicConfig(level=logging.INFO)

def main():
    # Note: 'hianime_bot_session' is just the session-file name. Change if you like.
    client = TelegramClient('hianime_bot_session', API_ID, API_HASH)

    # Register all your handlers (from handlers.py) exactly as before
    register_handlers(client)

    # Start the client in “bot mode” (no interactive prompt)
    client.start(bot_token=BOT_TOKEN)
    print("🚀 Bot is running (using BOT_TOKEN)…")
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
