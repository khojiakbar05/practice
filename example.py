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


print("============= ARRAY ===============")
from array import array

numbers = array("i", [1, 4, 3, 34, 54, 4])
print(numbers)

numbers.insert(3, 100)
print(numbers)

del numbers[0:3]
print(numbers)


numbs = array("i", [23, 1, 4, 6, 54, 67, 4, 4, 1, 67, 23])
numbs_set = set(numbs)
print("numbs_set: ", numbs_set)


a = {20, 30, 40, 50}
b = {40, 50, 60}

result1 = a | b
result2 = a & b
result3 = a - b
result4 = a ^ b


print("result1 | : ", result1)
print("result2 & : ", result2)
print("result3 - : ", result3)
print("result4 ^ : ", result4)



def greeting(*args, **kwargs):
       print("*args: ", args)
       print("**kwargs: ", kwargs)


greeting("hi", 12, True, name="Khoji")

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (11, 21, 31, 41, 51, 61)

zipped = zip(tuple1, tuple2)
print(zipped)
print(list(zipped))


