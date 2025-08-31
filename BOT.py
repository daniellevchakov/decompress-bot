from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Replace with your bot token from @BotFather
BOT_TOKEN = '8276782691:AAEASgnJsE80hVKo3ywKyHzfw2R-znlT3iYOT_TOKEN_HERE'

# Define a dictionary of materials and decomposition times
DECOMPOSITION_TIMES = {
    "plastic": "♻️ Plastic takes approximately 450 years to decompose.",
    # you can add more materials here if needed
}

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me a material like 'plastic', and I'll tell you how long it takes to decompose.")

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    response = DECOMPOSITION_TIMES.get(text, "I don't know how long that takes to decompose.")
    await update.message.reply_text(response)

# Main function
def main():
    app = ApplicationBuilder().token("8276782691:AAEASgnJsE80hVKo3ywKyHzfw2R-znlT3iY").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()