'''
This file contains the main entry point for the Telegram bot.
'''
from telegram_bot import TelegramBot
import logging
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# Create an instance of the TelegramBot class
bot = TelegramBot()
# Start the bot
bot.start()