# numbers = {"1", "2", "3"}
# cars = ("BMW", "Mers", "ferrari")
# animals = ["Cow", "Rabbit"]

# for car in cars:
#     print(f"The cars: {cars}")

# for number in numbers:
#     print(f"the numbers: {numbers}")

# letters = list("Hello, How do you do")
# print(f"the xecution of list: {letters} and size {len(letters)}")


# fruits = ["apple", "banana", "kivi", "lemon"]
# a = fruits[2]
# b = fruits[1:3]
# c = fruits[::3]
# d = fruits[::-3]


# print("result: 1 ", a)
# print("result: 2 ", b)
# print("result: 3 ", c)
# print("result: 4 ", d)


# print("(======= list methods =========)")

# numbs = ["1", "2", "3"]
# print("numbs: ", numbs)
# # numbs.append("4")

# # numbs.insert(0, "5")

# # result = numbs.pop()

# # result = numbs.pop(0)

# # numbs.remove("1")

# # del numbs[0:2]

# # result = numbs.index("1")

# numbs.clear()
# print("numbs: ", numbs)
# # print("result: ", result)


# animals = ["Cow", "Rabbit", "fish"]
# numbers = {"1", "2", "3"}

# if "0" in numbers:
#     print("number have in this list")
# else:
#     print("didn't found the number")


# numbs1 = [2, 34, 6, 23, 3, 56, 65,]
# numbs1.sort()
# print("srted numbs1: ", numbs1)

# numbs1.sort(reverse=True)
# print("sorted reverse: ", numbs1)

# print("======== Lambda function =========")


# def multiply(x, y):
#     return x * y


# result = multiply(2, 6)
# print("multiply: ", result)
# # print(multiply(2, 5))


# people = [
#     ("Robert", 20, "B"),
#     ("Steve", 19, "C"),
#     ("Joseph", 25, "A"),
#     ("Michael", 30, "E"),
#     ("Ali", 40, "D")
# ]

# people.sort()
# print("people sort (1): ", people)


# people.sort(key=lambda student: student[2])
# print("people sort (2): ", people)


# print("======== Enumerate, map and filter =========")

# animals = ["Cow", "Rabbit", "fish"]

# for ele in enumerate(animals):
#     print("animals: ", ele)


# car_obj = dict(brand="ferrari", year=2026)
# car = car_obj.get("brand")
# print("car: ", car)
# car_year = car_obj.get("year")
# print("car_year: ", car_year)


# cars = [
#     ("Ferrari", 78),
#     ("Toyota", 87),
#     ("Audi", 116),
#     ("BMW", 109),
#     ("Pagani", 33)
# ]
# new_cars = []

# for car in cars:
#     new_cars.append(0)
# print("new_cars(1): ", new_cars)

# result1 = map(lambda car: car[0], cars)
# print(f"the result1: {result1} and {type(result1)}")

# new_cars = list(result1)
# print("new_cars: ", new_cars)

# print("======= filter ========")

# result_filter = filter(lambda car: car[1] > 80, cars)
# print(f"the result_filter: {result_filter}, and {type(result_filter)}")

# print(list(result_filter))
# # result_filter = list(result_filter)
# # print("filter: ", result_filter)

# math = [21, 32, 54, 76, 3, 43, 34, 65, 45]

# res_filter = list(filter(lambda num: num > 50, math))
# print(list(res_filter))


# print("============= ARRAY ===============")
# from array import array

# numbers = array("i", [1, 4, 3, 34, 54, 4])
# print(numbers)

# numbers.insert(3, 100)
# print(numbers)

# del numbers[0:3]
# print(numbers)


# numbs = array("i", [23, 1, 4, 6, 54, 67, 4, 4, 1, 67, 23])
# numbs_set = set(numbs)
# print("numbs_set: ", numbs_set)


# a = {20, 30, 40, 50}
# b = {40, 50, 60}

# result1 = a | b
# result2 = a & b
# result3 = a - b
# result4 = a ^ b


# print("result1 | : ", result1)
# print("result2 & : ", result2)
# print("result3 - : ", result3)
# print("result4 ^ : ", result4)



# def greeting(*args, **kwargs):
#        print("*args: ", args)
#        print("**kwargs: ", kwargs)


# greeting("hi", 12, True, name="Khoji")

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (11, 21, 31, 41, 51, 61)

# zipped = zip(tuple1, tuple2)
# print(zipped)
# print(list(zipped))


# list comprehensions: a)
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]

print(f"list_numbers: {list_numbers}, and type: {type(list_numbers)}")
print(numbers is list_numbers)

print(id(numbers), id(list_numbers))

list_numbers = numbers
print(id(numbers), id(list_numbers))
print(numbers is list_numbers)


# list comprehensions: b)
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
# list_people = map(lambda person: person[0], people)
# print("people's name: ", list(list_people))
list_person = [person[1] for person in people]
print(list_person)


# list comprehensions: c)
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

# list_cars = [car[0] for car in cars]
# print("list_cars: ", list_cars)

# list_cars = map(lambda car: car[0], cars)
# print("list car in lambda: ",  list(list_cars))


print("========== Set and List comprehension ============")

numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbers = {*numbs}

print(f"set_numbers: {set_numbers}, and type: {type(set_numbers)}")


# b version
dict_person_list = [person[0] for person in people]
print(f"dict_person_list: {dict_person_list}, and type: {type(dict_person_list)}")

dict_person_dict = {person[0]: person[1] for person in people}
print(f"dict_person_dict: {dict_person_dict}, and {type(dict_person_dict)}")


# c version
dict_person = {person[0]: person[1] for person in people if person[1] > 20}
print(f"dict_person: {dict_person}, and type: {type(dict_person)}")

dict_person_filter = filter(lambda person: person[1] > 20, people)
print(f"dict_person_filter: {list(dict_person_filter)} and type: {type(dict_person_filter)}")


import turtle

# Ekranni sozlash
screen = turtle.Screen()
screen.bgcolor("#f0f8ff")
screen.title("Python Turtle Pizza")

t = turtle.Turtle()
t.speed(13)  # Eng tez chizish


def draw_circle(radius, color, border_color, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(border_color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# 1. Pissa xamiri (Crest)
draw_circle(160, "#D2691E", "#8B4513", 0, 0)

# 2. Pishloq va sous (Cheese)
draw_circle(145, "#FFD700", "#FF8C00", 0, 0)

# 3. Pissa bo'laklari (Slices)
t.color("#8B4513")
t.pensize(2)
for i in range(8):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 45)
    t.pendown()
    t.forward(145)

# 4. Pepperoni (Kolbasalar)
pepperoni_locs = [
    (60, 60), (-60, 60), (60, -60), (-60, -60),
    (100, 0), (-100, 0), (0, 100), (0, -100)
]
for x, y in pepperoni_locs:
    draw_circle(20, "#B22222", "#800000", x, y)

# 5. Zaytun donachalari (Olives)
olive_locs = [
    (30, 30), (-30, 30), (30, -30), (-30, -30),
    (80, 40), (-80, -40), (40, 80), (-40, -80)
]
for x, y in olive_locs:
    draw_circle(5, "#2F4F4F", "black", x, y)

# Markazdagi kichik turtle belgisi (Oshpaz)
t.penup()
t.goto(0, -10)
t.color("green")
t.shape("turtle")
t.stamp()

t.hideturtle()
print("Pissa tayyor! Yoqimli ishtaha!")
turtle.done()
