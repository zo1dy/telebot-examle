""" telegram bot example """
import sys
import os
import time
import logging
from dotenv import load_dotenv
import telebot
from telebot import types
from jinja2 import Environment, FileSystemLoader

# logging
#logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# load env
load_dotenv()
if not os.getenv('TOKEN'):
    print('Where is my TOKEN ?!')
    exit(1)
TOKEN = os.getenv('TOKEN')

# templates messages
env = Environment(loader=FileSystemLoader('templates'))
template_exapmle = env.get_template('example.txt')

def main():
    bot = telebot.TeleBot(TOKEN, parse_mode=None)

    while True:
        msg = template_exapmle.render({'username':'Дмитрий'})
        bot.send_message(-1001384310733, msg)
        time.sleep(5)
    # infinity
    bot.infinity_polling(skip_pending=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
