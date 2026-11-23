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
    CHAT_ID= os.getenv("CHAT_ID")

    app=ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.Chat(chat_id=CHAT_ID),echo))
    app.job_queue.run_daily(tenAM,time(10,0,tzinfo=zoneinfo.ZoneInfo("Europe/Warsaw")))




    app.run_polling()


async def start(update,context):
    name=update.effective_user.first_name
    await update.message.reply_text(f"Witaj, {name}")

async def echo(update,context):
    await update.message.reply_text(update.message.text)


async def tenAM(context):
           
    return


if __name__ == "__main__":
    main()