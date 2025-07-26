# File: /telegram-bot-app/telegram-bot-app/src/telegramBot.py

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am Alame\'s Bitch. How can I assist you with my butthole today\nAlso i can predict your haouse value?')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('دستورات ربات:\n/start - شروع\n/help - راهنما\nارسال هر پیام دیگر: پاسخ همان پیام\nارسال عکس: دریافت پیام مخصوص عکس')

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('عکس دریافت شد!')

def main() -> None:
    app = ApplicationBuilder().token("7664254505:AAHaAdGesCnQvuQL5IBFikhvL3Kyv219FlE").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

    app.run_polling()

if __name__ == '__main__':
    main()