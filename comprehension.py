''' Comprehension 
       (1) What is comprehension & list comprehension
       (2) Set and List comprehension
'''

print("========== What is comprehension & list comprehension ============")
# Comprehension boshqa tillardagi spread operator pythonda comprehension deyiladi va hosil qilinadi


''' Comprehension general syntax:
       a) *iterable
       b) <expression> for item in iterable
       c) <expression> for item in iterable <consition>
'''

# list comprehensions: a)
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
# list_numbers = numbers   -> bu holatda referencei bir hil boladi va true qaytaradi
print("list_numbers: ", list_numbers)
print(numbers is list_numbers)

print(id(numbers), id(list_numbers))

print("----------")

# list comprehensions: b)
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]

list_people = [person[0] for person in people]
print("list_people: ", list_people)
# res_map = map(lambda name: name[0], people)
# print(list(res_map))

# res_filter = filter(lambda person: person[1] > 20, people)
# print("res_filter: ", list(res_filter))


print("----------")


# list comprehensions: c)
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

list_cars = [car[1] for car in cars if car[1] > 80]
print("list_cars: ", list_cars)


print("========== Set and List comprehension ============")

numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs: ", set_numbs)


dict_people = {person[0]: person[1] for person in people}  # b - version 
print("dict_people: ", dict_people)

dict_people = {person[0]: person[1] for person in people if person[1] > 20}  # c - version
print("dict_people(2): ", dict_people)

# <expression> for item in iterable.   generic
