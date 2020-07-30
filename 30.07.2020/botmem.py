import telebot
import config
from collections import defaultdict

USER_STATE = defaultdict(lambda: START)
START, TITLE, PRICE, CONFIRMATION = range(4)

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda message: get_state(message) == START)
def handle_message(message):
    bot.send_message(message.chat.id, text='Напиши название.')
    update_state(message, TITLE)


@bot.message_handler(func=lambda message: get_state(message) == TITLE)
def handle_title(message):
    # название
    update_product(message.chat.id, 'title', message.text)
    bot.send_message(message.chat.id, text='Укажи цену.')
    update_state(message, PRICE)


@bot.message_handler(func=lambda message: get_state(message) == PRICE)
def handle_price(message):
    # название
    update_product(message.chat.id, 'price', message.text)
    product = get_product(message.chat.id)
    bot.send_message(message.chat.id, text='Опубликовать объявление? {}'.format(product))
    update_state(message, CONFIRMATION)


@bot.message_handler(func=lambda message: get_state(message) == CONFIRMATION)
def handle_confirmation(message):
    if 'да' in message.text.lower():
        bot.send_message(message.chat.id, text='Объявление опубликовано')
    update_state(message, START)


PRODUCTS = defaultdict(lambda: {})


def update_product(user_id, key, value):
    PRODUCTS[user_id][key] = value


def get_product(user_id):
    return PRODUCTS[user_id]


def get_state(message):
    return USER_STATE[message.chat.id]


def update_state(message, state):
    USER_STATE[message.chat.id] = state


bot.polling()
