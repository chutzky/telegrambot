import os
import logging
from datetime import time
import zoneinfo
import dotenv
import telegram
from telegram.ext import(ApplicationBuilder,CommandHandler,MessageHandler,filters,ContextTypes)

your_message="Tabletki"


def main():
    dotenv.load_dotenv()
    TOKEN=os.getenv("BOT_TOKEN")
    CHAT_ID= os.getenv("CHAT_ID")

    app=ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,deleteFirstReminder))

    app.job_queue.run_daily(remidner,time(10,0,tzinfo=zoneinfo.ZoneInfo("Europe/Warsaw")),name="tenAM")

    app.job_queue.run_daily(remidner,time(18,0,tzinfo=zoneinfo.ZoneInfo("Europe/Warsaw")),name="sixPM")


async def start(update,context):
    name=update.effective_user.first_name
    await update.message.reply_text(f"Witaj, {name}")


async def remidner(context):
    CHAT_ID= os.getenv("CHAT_ID")
    if not context.job_queue.get_jobs_by_name("everyhour"):
        context.job_queue.run_repeating(hourlyReminder,interval=3600,first=3600,name="everyhour")
    await context.bot.send_message(chat_id=CHAT_ID,text=your_message)

async def hourlyReminder(context):
    CHAT_ID= os.getenv("CHAT_ID")
    await context.bot.send_message(chat_id=CHAT_ID, text=your_message)
    

async def deleteFirstReminder(update,context):
    text=update.message.text.strip().lower()
    if text == "ok":
        for i in context.job_queue.get_jobs_by_name("everyhour"):
            i.schedule_removal()
            await update.message.reply_text("Uszanowanko")






if __name__ == "__main__":
    main()