# main.py

import os
import logging
import threading
from telethon import TelegramClient
from handlers import register_handlers
from flask import Flask
from dotenv import load_dotenv

# --------------------------------------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------------------------------------
load_dotenv()

API_ID   = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

if not (API_ID and API_HASH and BOT_TOKEN):
    raise RuntimeError("API_ID, API_HASH, and BOT_TOKEN must be set in your .env")

# --------------------------------------------------------------------------------
# 2. Simple Flask app for Render’s port‐binding checks
# --------------------------------------------------------------------------------
app = Flask(__name__)

@app.route("/")
def health_check():
    return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# --------------------------------------------------------------------------------
# 3. Main Telethon bot logic (exactly as before, but using bot_token)
# --------------------------------------------------------------------------------
def main():
    logging.basicConfig(level=logging.INFO)

    # Create TelegramClient and register handlers
    client = TelegramClient('hianime_bot_session', API_ID, API_HASH)
    register_handlers(client)

    # Start in “bot” mode so it never prompts for phone/code
    client.start(bot_token=BOT_TOKEN)
    print("🚀 Bot is running…")

    # Run until disconnected
    client.run_until_disconnected()


# --------------------------------------------------------------------------------
# 4. Entry point: spin up Flask in a background thread, then run the bot
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    # Start Flask on a separate thread so Render sees an open port
    threading.Thread(target=run_flask, daemon=True).start()

    # Then start the Telethon bot
    main()
