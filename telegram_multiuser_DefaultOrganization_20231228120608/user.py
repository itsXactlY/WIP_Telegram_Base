'''
This file contains the User class that represents a Telegram bot user.
'''
class User:
    def __init__(self, chat_id):
        '''
        Initialize a new User object with the given chat ID.
        '''
        self.chat_id = chat_id
        self.subscribed = False
    def subscribe(self):
        '''
        Subscribe the user to receive updates.
        '''
        self.subscribed = True
    def unsubscribe(self):
        '''
        Unsubscribe the user from receiving updates.
        '''
        self.subscribed = False