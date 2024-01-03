'''
This file contains the TelegramBot class that represents the Telegram bot.
'''
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from user import User
import encryption
import os
class TelegramBot:
    def __init__(self):
        '''
        Initialize a new TelegramBot object.
        '''
        self.users = {}
        self.api_key = encryption.decrypt_api_key()
    def start(self):
        '''
        Start the Telegram bot.
        '''
        # Create the Telegram updater and dispatcher
        updater = Updater(token=self.api_key, use_context=True)
        dispatcher = updater.dispatcher
        # Register command handlers
        start_handler = CommandHandler('start', self.start_command)
        subscribe_handler = CommandHandler('subscribe', self.subscribe_command)
        unsubscribe_handler = CommandHandler('unsubscribe', self.unsubscribe_command)
        unknown_handler = MessageHandler(Filters.command, self.unknown_command)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(subscribe_handler)
        dispatcher.add_handler(unsubscribe_handler)
        dispatcher.add_handler(unknown_handler)
        # Start the bot
        updater.start_polling()
    def start_command(self, update, context):
        '''
        Handle the /start command.
        '''
        chat_id = update.effective_chat.id
        if chat_id not in self.users:
            self.users[chat_id] = User(chat_id)
        context.bot.send_message(chat_id=chat_id, text='Welcome to the bot!')
    def subscribe_command(self, update, context):
        '''
        Handle the /subscribe command.
        '''
        chat_id = update.effective_chat.id
        if chat_id in self.users:
            user = self.users[chat_id]
            user.subscribe()
            context.bot.send_message(chat_id=chat_id, text='You have been subscribed.')
        else:
            context.bot.send_message(chat_id=chat_id, text='Please use the /start command first.')
    def unsubscribe_command(self, update, context):
        '''
        Handle the /unsubscribe command.
        '''
        chat_id = update.effective_chat.id
        if chat_id in self.users:
            user = self.users[chat_id]
            user.unsubscribe()
            context.bot.send_message(chat_id=chat_id, text='You have been unsubscribed.')
        else:
            context.bot.send_message(chat_id=chat_id, text='Please use the /start command first.')
    def unknown_command(self, update, context):
        '''
        Handle unknown commands.
        '''
        context.bot.send_message(chat_id=update.effective_chat.id, text='Unknown command. Please try again.')