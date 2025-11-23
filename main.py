BOT_TOKEN = "8580939622:AAFO29txXbEOCsXiWhkvM6aqGCx640iLvCQ"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Ye source channel (jaha se msgs aayenge)
SOURCE_CHAT_ID = -1001726875252

#Ye middle group (jaha ExtraPeBot message pickup karega)
DEST_GROUP_ID = -1002466550633
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


async def forward_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        #Check if message comes from source channel
        if update.effective_chat.id == SOURCE_CHAT_ID:

            #Forward to middle group
            await update.message.forward(chat_id=DEST_GROUP_ID)

    except Exception as e:
        print("Forward Error:", e)


async def print_updates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Use this handler only for debugging during first run
    print(update)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    #Auto-forward handler
    handler = MessageHandler(filters.ALL, forward_messages)
    app.add_handler(handler)

    print("Bot is running... Forwarding enabled!")
    app.run_polling()


if name == "main":
    main()
https://telegram-forward-bot-vmi9.onrender.com
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from flask import Flask
import threading

#==============================
BOT_TOKEN = "YOUR_BOT_TOKEN"
SOURCE_CHAT_ID = -1001726875252
DEST_GROUP_ID = -1002466550633
#==============================

app_flask = Flask(name)

@app_flask.route("/")
def home():
    return "Bot is running!"

async def forward_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.effective_chat.id == SOURCE_CHAT_ID:
            await update.message.forward(chat_id=DEST_GROUP_ID)
    except Exception as e:
        print("Forward Error:", e)

def start_flask():
    app_flask.run(host="0.0.0.0", port=10000)

def main():
    telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()
    telegram_app.add_handler(MessageHandler(filters.ALL, forward_messages))

    #run flask server in thread
    threading.Thread(target=start_flask).start()

    print("Bot started!")
    telegram_app.run_polling()

if name == "main":
    main()
