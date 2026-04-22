''' Tuples
       (1) What is tuple 
       (2) Unpacking Arguments
       (3) Zip
'''

print("======== What is tuple =========")
# Java / PhP / NodeJs => Python list
# boshqa tillardaagi listlar Pythinda list deb ataladi

# Literal -> usulda qurilishi
numbs = [3, 5, 1, 2]
print(numbs)


# constructor -> usulda qurilishi
letters = list("Hello World")
print(letters)


fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits: ", fruits)

fruits[2] = "melon"
print("after fruits: ", fruits)

#  TUPLE
# tupleni qiymatini ozgartira olmaymiz

animals = ("dog", "cat", "fish", "lion")
print("animals: ", animals)
tuple_obj = ("MIT", 100, True, None)
print("before tuple_obj: ", tuple_obj)

# animals[0] = "bird"
# print("after tuple_obj: ", tuple_obj)


# try void these:
people = "Andrew", "John"
animals = "dog",

print("======== Unpacking Arguments =========")
groups = ["MIT", "FLEX", "DEVEX", "MG"]
(x, y, a, z) = groups
# *z -> bu x va y ga tepadan qiymatlarni oladi va *ga qolga qiymatlarni kiritvoradi
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z: ", z)


# *args > tuple degani

def calculate(*args):
    total = 1
    for x in args:
       total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# call
calculate(1, 7, 2, 3)
print("------")
calculate(0, 2, 300)
print("------")
calculate(5, 7)


# **kwargs > dictionary orqali xosil bolgan tupleni yoyish
def introduce(*args, **kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I'm {kwargs["name"]} and I am {kwargs["age"]} years old")
    pass

# call 
introduce(name="Justin", age=25)
introduce(name="Shawn", age=30, single=True)

print("------")


def greeting(*args, **kwargs):
    print("*args: ", args)
    print("**kwargs: ", kwargs)
    

# Call
greeting("hi", True, 10, name="John", age=22)
# ( *args )    "hi", True, 10,      => bu qiymatlar tuple korinishida qabul qilinadi
# ( **kwargs ) name="John", age=22  => bu qiymatlarimiz keyword dictionary korinishida qabul qilinadi 


print("======== zip =========")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c', 'd')

zipped = zip(tuple1, tuple2)
print("zipped: ", zipped)
result = list(zipped)
print(f"the result: {result}")





