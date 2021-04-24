import telebot
from mtranslate import translate

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
    def get_instance(cls, user):
        if not cls._instance:
            cls._instance = controller(user)
        return cls._instance

class black_box:
    _instance = None
    def __init__(self):
        self.sys = {'Aa':'Алпресе Авиягро','Ab':'Антор Брукало','Ac':'Амер Салага'}#соотношения имён и сочетаний букв
        self.code = 'Никола Тесла'
        self.to_translate = ''
    def give_answer(self, x, d):
        self.to_translate = x
        m = translate(self.to_translate,'en')
        x = m[0] + m[len(m) - 1]
        x = self.sys[x]
        if(x == self.code):
            bot.send_message(message.from_user.id, 'Вы нашли Николу Теслу! Вы молодец!')
            d.finish()
        else:
            bot.send_message(message.from_user.id, 'Найден ', x)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = black_box()
        return cls._instance

API = '1693316060:AAFe5c3xHvy3kGmVyhHlKukFWqzb2ks1Ark'

bot = telebot.TeleBot(API)

a = ""
y = 0
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
    a = message.text
    d.play(message.from_user.id)

@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.from_user.id, "Поисковая система работает...")
    i.give_answer(a,d)
    if (d.users[message.from_user.id] == "Finish"):
        brake
    else:
        a = message.text
        
bot.polling()
