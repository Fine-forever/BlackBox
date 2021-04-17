from mtranslate import translate
class black_box:
    _instance = None
    def __init__(self):
        self.sys = {'Aa':'Алпресе Авиягро','Ab':'Антор Брукало','Ac':'Амер Салага'}#соотношения имён и сочетаний букв
        self.code = 'Никола Тесла'
        self.to_translate = ''
    def give_answer(self, x):
        self.to_translate = x
        m = translate(self.to_translate,'en')
        x = m[0] + m[len(m) - 1]
        x = self.sys[x]
        if(x == self.code):
            print('Вы победили!')
        else:
            print('Найден ',x)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = black_box()
        return cls._instance

i = black_box().get_instance()
i.give_answer('Америка')