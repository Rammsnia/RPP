# Классы и функции классов

# Для полиморфизма
class Car:
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def get_speed(self):
        return self.s / self.t
class Gravitation:

    def __init__(self, v):
        self.v = v
        self.c = 299792458

    def get_speed(self):
        return (self.v/self.c)**3

# Для наследования

# Класс предок

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print_name(self):
        print(f"Name: {self.name}")
    # Красиво выведем имя

    def Age(self):
        if self.age < 35:
            print(f"{self.name}: Молодой")
        else:
            print(f"{self.name}: Не молодой")


class Grandfather(People):
    def name_d(self):
        print(f"{self.name} - дед")

# Инкапсуляция

class private1:
    def _private(self):
        print("ЗаприваченО!")

class SuperPrivate:
    def __private(self):
        print("Супер-пупер Запривачено!")
