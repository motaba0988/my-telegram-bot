from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["8266260672:AAHCXzXfsaE3gmkFs5g0-faR43o38_W30NQ"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ ربات با موفقیت راه افتاد!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("ربات روشنه...")
app.run_polling()
