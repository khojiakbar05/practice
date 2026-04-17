''' OBJECTS:
   (1) What is object?
   (2) Iterable objects & RANGE
   (3) DICTIONARY
   (Error handling system
'''


import math  # Pythondan mustaqil va python bilan birga keladi va inputni talab qiladigon package hisoblanadi
import array  # package / module => python bilan birga paralel kun koradi

from math import ceil, asin  # yana bir yoli chaqirishni va packagelari qoshib ketsa boladi va bu methodlarni aniq qilib chaqirib olish used
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


