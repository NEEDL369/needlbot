import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

SPINS = [
    "🌀 You spun the Spinner and got... NOTHING! Try again?",
    "💰 You hit a Micro Jackpot! 0.01 $NEEDL coming your way... maybe 😏",
    "🎉 Bonus spin unlocked (coming soon)",
    "🚀 You found a rare airdrop portal! [Feature in progress]",
    "😅 Just wind... try again."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the $NEEDL Spinner! Type /spin to try your luck!")

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.choice(SPINS)
    await update.message.reply_text(result)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("spin", spin))

print("Bot is running...")
app.run_polling()
