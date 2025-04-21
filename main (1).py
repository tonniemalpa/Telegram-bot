from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Token
TOKEN = "8168523477:AAFbO9z8ENGGUOpmT4z21LNdIbElUIGUtI4"

# /start command
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Explore", callback_data='explore')],
        [InlineKeyboardButton("Learn", callback_data='learn')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to StarBot! Choose an option:", reply_markup=reply_markup)

# Button responses
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'explore':
        query.edit_message_text("You're exploring digital stars and constellations!")
    elif query.data == 'learn':
        query.edit_message_text("StarBot offers fun facts and cosmic insights!")

# Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()