import re

class Smartphone:
    def __init__(self, brand, model, number):
        if not re.match(r'^\+79\d{9}$', number):
            raise ValueError("Номер телефона должен быть в формате +79XXXXXXXXX")
        self.brand = brand
        self.model = model
        self.number = number

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.number}"