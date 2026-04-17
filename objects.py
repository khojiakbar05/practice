''' OBJECTS:
   (1) What is object?
   (2) Iterable objects & RANGE
   (3) DICTIONARY
   (4) Error handling system
'''


import math  # Pythondan mustaqil va python bilan birga keladi va inputni talab qiladigon package hisoblanadi
import array  # package / module => python bilan birga paralel kun koradi

# yana bir yoli chaqirishni va packagelari qoshib ketsa boladi va bu methodlarni aniq qilib chaqirib olish used
from math import ceil, asin
print("========= WWhat is Object ===========")
# (1) What is object?

# Object => Ma'lum bir maqsadda yaratilgan va ozini bir qator method ha,da propertylaridan tashkil topgan data type hisoblanadi.
# Everything is objet in PYTHON

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# Paradigms => Functional programming   &.  OOP
# OOP 4 conceptions: => Abstraction & Encapsulation & Inheritance & Polymorphism

result = math.ceil(97.7)  # call
print("result: ", result)

result = ceil(98.7)
print("result1: ", result)


print("========== Error handling System =============")

car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["year"]
    print("result: ", result)
    # ikkala xatolik turini bitta shartda berishimiz uchun mana bunday qiamiz
    # except (KeyError, AttributeError) as err:      => shukorinishda beriladi
    '''hamma xatolik turini mujassamlagan bu => (exception) boladi ishlatilish'''
    # except exception as err:         => mana shu korinishda
except KeyError as err:
    print("No origin state property found: ", err)
except AttributeError as err:
    print("No speed found!!!")
else:
    print("Executed successfully!")
finally:  # oxirida ishga tuhadigon. matiqimiz
    print("Final closing logic")
