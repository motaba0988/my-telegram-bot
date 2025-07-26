from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import random

words = [
    {
        "de": "der Hund",
        "fa": "سگ",
        "example_de": "Der Hund schläft unter dem Tisch.",
        "example_fa": "سگ زیر میز خوابیده است."
    },
    {
        "de": "das Buch",
        "fa": "کتاب",
        "example_de": "Ich lese ein Buch über Geschichte.",
        "example_fa": "من یک کتاب درباره تاریخ می‌خوانم."
    },
    {
        "de": "die Katze",
        "fa": "گربه",
        "example_de": "Die Katze sitzt auf dem Sofa.",
        "example_fa": "گربه روی مبل نشسته است."
    }
]

async def word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = random.choice(words)
    text = f"""📘 کلمه امروز:
**{word['de']}** = {word['fa']}

📝 مثال:
{word['example_de']}
({word['example_fa']})
"""
    await update.message.reply_text(text, parse_mode="Markdown")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 👋 برای دریافت کلمه‌ی آلمانی، بنویس /word")

TOKEN = os.environ["BOT_TOKEN"]
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("word", word))

print("ربات آموزش آلمانی روشنه...")
app.run_polling()
