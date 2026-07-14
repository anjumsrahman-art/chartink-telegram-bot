from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Chartink Telegram Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}

    message = f"📈 Chartink Alert\n\n{data}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return "OK", 200
