# -*- coding: utf-8 -*-

import telebot
from mtranslate import translate
import json

class controller:
    _instance = None
    def __init__(self):
        self.users = {}
    def start(self,user):
        self.users.update({user:'Greetings'})
    def play(self,user):
        self.users[user] = "Playing"
    def finish(self, user):
        self.users[user] = "Finish"
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = controller()
        return cls._instance

class black_box:
    _instance = None
    def __init__(self):
        with open("names_file.json","r") as read_file:
            self.sys = json.load(read_file)
        self.code = 'Никола Тесла'
        self.to_translate = ''
    def give_answer(self, x, d):
        self.to_translate = x
        try:
            m = translate(self.to_translate,'en')
            x = m[0] + m[len(m) - 1]
            x = self.sys[x]
            if(x == self.code):
                return 'Вы нашли Николу Теслу! Вы молодец! Вы можете посмотреть в поисковике других учёных, для прекращения работы напишите /end'
                d.finish()
            else:
                return 'Найден '+ x
        except Exception:
            return 'Пишите существующие русские слова с большой буквы!'

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = black_box()
        return cls._instance

API = '1693316060:AAFe5c3xHvy3kGmVyhHlKukFWqzb2ks1Ark'

bot = telebot.TeleBot(API)

i = black_box().get_instance()
d = controller().get_instance()

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
    d.start(message.from_user.id)
    bot.send_message(message.from_user.id, "Здравствуйте, адмирал. Колонизация Марса прошла почти успешно... Один учёный, а именно Никола Тесла , потерялся среди марсианских учёных. Перед вами поисковая система 'Турбо 2000' с русско-марсианским переводчиком. Поисковик способен принять только одно слово. Найдите Теслу!")
    d.play(message.from_user.id)

@bot.message_handler(commands=['end'])
def end(message):
    bot.send_message(message.from_user.id, 'Поисковик выключается.. Для повтора игры напишите /start')

@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.from_user.id, "Поисковая система работает...")
    bot.send_message(message.from_user.id,i.give_answer(message.text, d))

bot.polling()