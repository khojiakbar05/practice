''' LISTS 
       (1) Working with lists
       (2) List methods
       (3) Lambda function
       (4) Enumerate, map and filter
'''

print("======== Working eith lists =========")

# LITERL usulda qurish
person = {"name": "Justin", "age": 25}    # Dictionry usulda qurish
people = ("Andrew", "John", "Mihchael")   # TUuple usulda qurish
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # List usulda qurish
for team in groups:
    print(f"the team {team}")



# COnstructor
letters = list("HEllo World!")
print(f"the letters: {letters} and size: {len(letters)}")

print("--------")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # 0 dan 2 gacha olib beradi
c = fruits[::3]  # 0 ni oladi va orada 2ta index tashlab ketib 3 chini oladi
d = fruits[::-1] # teskari holatda listimizni qaytaradi

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)


print("======== List methods =========")
# methods => append(), insert(), pop(), remove(), clear(), sort(), index()

# Mutable(ozgaradi) => append(), insert(), pop(), remove(), clear(), sort()
# Immutable => index(),  sorted()
 
letters = ["a", "b", "d"]
letters.append("c")   # oxiridan list qoshadi
print(f"the append result {letters}")


letters.insert(0, "z")   # listni oldiga qiymat qoshadi
print(f"the insert result: {letters}")

size = len(letters) -1
result = letters.pop(size)  # pop listni oxiridan qiymatni  qirqib oladi
print(f"the pop result: {result} and letter: {letters}") 


result2 = letters.pop(0)  # pop listimizni birinchi qiymatini olib beradi
print(f"the pop result2: {result} and letter: {letters}")


print("--------")
animals = ["dog", "cat", "capybara", "fish", "lion"]

print("animlas: ", animals)

animals.remove("lion")   # listni qiymatini ochirib tashlaydi
print("remove: ", animals)


del animals[2:4]   # del belgilangan indexlar orasini ochirib tashlaydi  
print("animals delete: ", animals)

exit = animals.index("cat")   # qiymat listni ichida bolsa indexini chiqazadi
print("index: ", exit)

animals.clear()  # listni hamma qiymatini ochirib tashleydi
print("clear: ", animals)

if "cat" in animals:
    print("indexOf cat: ", animals.index("cat"))
else:
    print("cat does not ezist")


print("--------")
numbers = [2, 20, 12, 8, 57]
numbers.sort()   #. listimizni qiymatlarini tartiblab beradi
print("numbers sort: ", numbers)

numbers.sort(reverse=True)  # . listimizni qiymatlarini teskari tartibda qilib beradi
print("sort reverse: ", numbers)


# Immutable sorted(), index()
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"th sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("======== Lambda function =========")
# lambda is small anonymous function!
def calculate(x, y): return x * y

result = calculate(3, 5)
print("result: ", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()  # oddiy sortda alphabit boyicha sort qiladi
print("People(1) ", people)

# lambda by age ia sorted yoshga nisbatan sort qilish
people.sort(key=lambda person: person[1])
print("People(2) ", people)


print("======== Enumerate, map and filter =========")
# Enumerate for index & value qabul qilish

animals = ["dog", "cat"]
for element in enumerate(animals):   # valueni Indexini ham oilib beradi
     print("element: ", element)


print("--------")
for (index, value) in enumerate(animals):   # 
    print(f"the index: {index}, value: {value}")



# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)
# result = car_obj.get("brand")
result = car_obj.items()  # tuple korinishida qaytaradi
for (key, value) in result:
    print(f"the key: {key}, value: {value}")


print("---- map ----")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_cars(1) ", new_cars)


result1 = map(lambda car: car[0], cars)
print(f"the result1: {result1} and type: {type(result1)}")

new_cars = list(result1)
print("new_cars(2)", new_cars)


print("---- filter ----")
# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))

