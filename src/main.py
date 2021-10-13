import telebot
import os
from loguru import logger
from telebot import types
from src.utils import create_keyboard
from src.constants import keyboards

class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(
        os.environ['TELEGRAMBOT_TOKEN'],
        parse_mode='HTML'
        ) # You can set parse_mode by default. HTML or MARKDOWN
        self.respond_welcome = self.bot.message_handler(commands=['start', 'help'])(self.respond_welcome)
        self.respond_text = self.bot.message_handler(func=lambda message: True)(self.respond_text)


    def respond_welcome(self, message):
        self.set(message)
        self.bot.send_message(
            message.chat.id,
            f"Howdy, how are you doing <b>{self.name}</b>?",
            reply_markup=keyboards['main']
            )


    def respond_text(self, message):
        self.set(message)
        self.bot.send_message(
            message.chat.id,
            f'Hiiiiii <b>{self.name}</b>')

    def run(self):
        logger.info('Running Bot ...')
        self.bot.polling()

    def set(self, message):
        self.name = message.chat.first_name
        if message.chat.last_name:
            self.name = f'{self.name} {message.chat.last_name}'
        self.chat_id = message.chat.id
        logger.info(self.chat_id)

if __name__ == '__main__':
    bot = Bot()
    bot.run()

