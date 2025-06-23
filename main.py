import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Your bot token
BOT_TOKEN = "7579053949:AAG5VKJQ9RMY7TM2RTbOtf-7FhOu7hz42wg"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Bitnodes Signal Bot!\nUse /signal to get trading signals.")

# /signal command
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Sample dummy signal
    example_signal = "🔔 Signal: LONG BTC/USDT\nEntry: 65000\nSL: 64200\nTP: 66800"
    await update.message.reply_text(example_signal)

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    app.run_polling()

if __name__ == '__main__':
    main()
