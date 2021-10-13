import os

import telebot
from loguru import logger
from telebot import types
import emoji
from src.constants import KEYBOARDS
# from src.utils import create_keyboard


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
        self.send_message(
            f"Howdy, how are you doing <b>{self.name}</b>?",
            reply_markup=KEYBOARDS.main
            )

    def respond_text(self, message):
        self.set(message)
        self.send_message(
            f'Hiiiiii <b>{self.name}</b>')
    
    def send_message(self, bot_response, chat_id=None, reply_markup=None, emojize=True):
        if emojize:
            bot_response = emoji.emojize(bot_response)
        if not chat_id:
            chat_id = self.message.chat.id
        self.bot.send_message(chat_id, bot_response, reply_markup=reply_markup)

        
    def run(self):
        logger.info('Running Bot ...')
        self.bot.polling()

    def set(self, message):
        self.message = message
        self.name = message.chat.first_name
        if message.chat.last_name:
            self.name = f'{self.name} {message.chat.last_name}'
        self.chat_id = message.chat.id
        logger.info(self.chat_id)


if __name__ == '__main__':
    bot = Bot()
    bot.run()
