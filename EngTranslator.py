
from time import sleep
from random import randint
from googletrans import Translator, constants
tr = Translator()

def toEng(statement = '', lan = ''):
    if lan != 'en':
        sleep(randint(1, 5))
        return tr.translate(statement, dest = 'en').text
    else:
        return statement
