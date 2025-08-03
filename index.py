import string

from random import choice, randint
from config import MAX_PRICE, MIN_PRICE

TOMATO_LIST = [ ]

class Tomato:
    def __init__(self, price, tag):
        self.price = price
        self.tag = tag

    def generate_tag(self, length=6):
        symbols = string.ascii_uppercase + string.digits
        tag = ""

        for _ in range(length):
            tag += choice(symbols)
        return tag
    
    def generate_fake_tomatoes(self, times=50):
        for _ in range(times):
            price = randint(MIN_PRICE, MAX_PRICE)
            tag = self.generate_tag()
            TOMATO_LIST.append(Tomato(price, tag))

        return TOMATO_LIST

    def filter_by(**kwargs):
        for key, value in kwargs.items():
            if key.endswith("__gt"):
                result = [tomato for tomato in TOMATO_LIST if tomato.price > value]
            elif key.endswith("__lt"):
                result = [tomato for tomato in TOMATO_LIST if tomato.price < value]
                
        return result
    
    def start():
        Tomato(0, "").generate_fake_tomatoes()
        filtered_tomatoes = Tomato.filter_by(price__gt=6)
        
        for tomato in filtered_tomatoes:
            print(f"Price: {tomato.price}, Tag: {tomato.tag}")

Tomato.start()
