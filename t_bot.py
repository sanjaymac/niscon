import asyncio
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

nest_asyncio.apply()

BOT_TOKEN = "7863227666:AAE-zzVjo02h7hqOGZaB7xT1pEdmon02bQ8"

MOVIE_LINKS = {
    "seven doors": ("Seven Doors", "https://t.me/pbxs1/2"),
    "lisabi": ("Lisabi", "https://t.me/pbxs1/3")
}

async def reply_movie_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    if user_text in MOVIE_LINKS:
        name, url = MOVIE_LINKS[user_text]
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text=name, url=url)]])

        sent_msg = await update.message.reply_text(
            "🎥 *Movie link found!*\n\n"
            "Click the button below to open the movie link.\n"
            "🕒 This message will disappear in 2 minutes.",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

        await asyncio.sleep(120)  # Auto-delete in 2 minutes
        try:
            await context.bot.delete_message(chat_id=sent_msg.chat_id, message_id=sent_msg.message_id)
        except Exception as e:
            print(f"Failed to delete message: {e}")
    else:
        await update.message.reply_text(
            "❌ Sorry, only *'seven doors'* or *'lisabi'* are available right now.",
            parse_mode="Markdown"
        )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), reply_movie_link)
    app.add_handler(handler)

    print("🤖 Bot running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
