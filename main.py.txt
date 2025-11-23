rom telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8580939622:AAFO29txXbEOCsXiWhkvM6aqGCx640iLvCQ"
SOURCE_CHANNEL = -1001726875252 # Replace with source channel ID
DEST_CHANNEL = -1002466550633 # Replace with destination channel ID

def forward_message(update, context):
    context.bot.forward_message(
        chat_id=DEST_CHANNEL,
        from_chat_id=SOURCE_CHANNEL,
        message_id=update.message.message_id
    )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.chat(SOURCE_CHANNEL), forward_message))

updater.start_polling()
updater.idle()