import telebot
import os
from loguru import logger

class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(
        os.environ['TELEGRAMBOT_TOKEN'],
        parse_mode=None
        ) # You can set parse_mode by default. HTML or MARKDOWN
        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)


    def send_welcome(self, message):
	    self.bot.reply_to(message, "Howdy, how are you doing?")


    def echo_all(self, message):
    	self.bot.reply_to(message, message.text)

    def run(self):
        logger.info('Running Bot ...')
        self.bot.polling()


if __name__ == '__main__':
    bot = Bot()
    bot.run()
    



# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# print('Starting bot.....')
# bot.polling()