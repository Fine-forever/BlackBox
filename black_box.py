import requests
from bs4 import BeautifulSoup
class black_box:
    _instance = None
    def __init__(self):
        self.sys = {'Aa' : 'Алпресе Авиягро'}#соотношения имён и сочетаний букв
        self.code = 'Никола Тесла'
        self.r = requests.get('translate.google.com')
        self.soup = BeautifulSoup(self.r.text, 'lxml')
    def give_answer(self, x):
        self.r.params = '?sl=ru&tl=en&text='+x+'&op=translate'
        m = self.soup.find_all('c-wiz', class_='text')
        #будет возвращать перевод, брать буквы и сверять со словарём

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = black_box()
        return cls._instance


