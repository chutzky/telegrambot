import os
import logging
from datetime import time
import zoneinfo
import dotenv
import telegram
from telegram.ext import(ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes)


def main():
    dotenv.load_dotenv()
    TOKEN=os.getenv("BOT_TOKEN")

    app=ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,echo))





    app.run_polling()


async def start(update,context):

    await update.message.reply_text("Witam")

async def echo(update,context):
    await update.message.reply_text(update.message.text)

if __name__ == "__main__":
    main()