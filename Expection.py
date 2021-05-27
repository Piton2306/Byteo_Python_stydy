"""Обработка исключений"""
try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))


"""Вызов исключения"""


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = 'Введите что нибуть'
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("Зачем сделали EOF")
except ShortInputException as ex:
    print(("ShortInputException: Длина введённой -- {0}:"
           "ожидалось,как минимум,{1}".format(ex.length, ex.atleast)))
else:
    print("Не было исключений")
