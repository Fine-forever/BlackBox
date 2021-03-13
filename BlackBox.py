import telebot
import requests

class controller:
    def __init__(self, user):
        self.users = {user : "Greetings"}
    def play(self,user):
        self.users{user} = "Playing"

class black_box:
    def __init__(self):
        self.sys = {}#соотношения имён и сочетаний букв
        self.code = 'Никола Тесла'

API = '1693316060:AAFe5c3xHvy3kGmVyhHlKukFWqzb2ks1Ark'

bot = telebot.TeleBot(API)

x = ""

@bot.message_handler(content_types=['voice'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ошибка: аудиосообщения не принимаются")

@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ошибка: изображения не принимаются")

@bot.message_handler(content_types=['picture'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ошибка: изображения не принимаются")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "Здравствуйте, адмирал. Колонизация Марса прошла почти успешно... Один учёный, а именно Никола Тесла , потерялся среди марсианских учёных. Перед вами поисковая система 'Турбо 2000' с русско-марсианским переводчиком. Поисковик способен принять только одно слово. Найдите Теслу!")
    x = message.text
    user = controller(x = 2)

@bot.message_handler(content_types=['text'])
def start_message(message):
    user.play(x)
    bot.send_message(message.from_user.id, "Поисковая система работает...")
    #бот работает
    x = message.text