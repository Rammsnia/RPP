# Полиморфизм

from main import Car
from main import Gravitation
from main import People
from main import Grandfather
from main import private1
from main import SuperPrivate


carOne = Car(100, 10)
print(carOne.get_speed())

gravOne = Gravitation(10000)
print(gravOne.get_speed())

ded1 = Grandfather("Tom", 30)

ded1.Age()

a = private1()
a._private()
b = SuperPrivate()
b.__private()