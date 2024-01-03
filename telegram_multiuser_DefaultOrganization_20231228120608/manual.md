# Telegram Bot User Manual

## Introduction

The Telegram Bot is a Python-based application that allows users to interact with a Telegram bot through various commands. It supports multiple users and subscription functionality, ensuring comprehensive security measures and maintaining the integrity of user interactions. The bot incorporates robust encryption techniques to safeguard critical data, specifically API keys. It uses a non-SQL server database solution for storing user information.

## Installation

To install and run the Telegram Bot, follow these steps:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/your_username/telegram-bot.git
   ```

2. Navigate to the project directory:

   ```
   cd telegram-bot
   ```

3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Create a new file named `api_key.txt` and add your Telegram API key to it.

5. Run the bot:

   ```
   python main.py
   ```

## Usage

Once the Telegram Bot is up and running, you can interact with it using the following commands:

- `/start`: Start the bot and register as a user.
- `/subscribe`: Subscribe to receive updates from the bot.
- `/unsubscribe`: Unsubscribe from receiving updates.

## Example

Here's an example of how to use the Telegram Bot:

1. Start the bot by sending the `/start` command.
2. Subscribe to receive updates by sending the `/subscribe` command.
3. The bot will send you a confirmation message.
4. You will start receiving updates from the bot.
5. To unsubscribe, send the `/unsubscribe` command.

## Security

The Telegram Bot ensures the security of critical data, such as API keys, through robust encryption techniques. The `encryption.py` module handles the encryption and decryption of the API key. The encrypted API key is stored in the `api_key.txt` file, which is read by the bot during startup.

## Database

The Telegram Bot uses a non-SQL server database solution for storing user information. The `users` dictionary in the `TelegramBot` class maintains a mapping of user chat IDs to `User` objects. Each `User` object represents a Telegram bot user and stores information such as the chat ID and subscription status.

## Conclusion

The Telegram Bot provides a Python-based solution for building a Telegram bot with support for multiple users and subscription functionality. It incorporates robust encryption techniques to safeguard critical data and uses a non-SQL server database solution for storing user information. By following the installation and usage instructions provided in this manual, you can easily set up and use the Telegram Bot for your own purposes.