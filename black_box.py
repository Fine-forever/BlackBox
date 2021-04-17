import requests
from bs4 import BeautifulSoup
class black_box:
    _instance = None
    def __init__(self):
        self.sys = {'Aa':'Алпресе Авиягро','Ab':'Антор Брукало','Ac':'Амер Салага'}#соотношения имён и сочетаний букв
        self.code = 'Никола Тесла'
        self.r = requests.get('https://translate.google.com/')
        self.soup = BeautifulSoup(self.r.text, 'lxml')
        self.paramz = ''
    def give_answer(self, x):
        self.paramz = '?sl=ru&tl=en&text='+x+'&op=translate'
        self.r = requests.get('https://translate.google.com/', params = self.paramz)
        self.soup = BeautifulSoup(self.r.text, 'lxml')
        m = self.soup.find_all('span', class_='VIiyi')
        #будет возвращать перевод, брать буквы и сверять со словарём
        print(m)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = black_box()
        return cls._instance

i = black_box().get_instance()
i.give_answer('электричество')