
from time import sleep
from random import randint
from googletrans import Translator, constants
tr = Translator()

def toEng(statement = 'text to translate', lan = 'language abbreviation'):
    if lan != 'en':
        sleep(randint(1, 10))
        return tr.translate(statement, dest = 'en').text
    else:
        return statement
