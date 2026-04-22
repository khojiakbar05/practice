'''.   Loop operator
       (1) for 
       (2) Break / else
       (3) while
'''


print("========== for operator ===========")
# Iterable objects: => string, dict, tuple, list, range, map, filter

text = "MIT"
numbs = [10, 7, 3, 4]  # -> list
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

    print("-------")


for number in numbs:
    print(f"the numer: {number}")

    print("-------")


for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

    print("-------")
for x in range(1, 20, 5):
    print(f"the {x}")


    print("========== break / else ===========")

for x in range(1, 20, 5):
    print(f"the {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Looped successfully!")


    print("========== While ===========")

num = 40
while num > 0:
    num -= 10
    print(f"the number equals: {num}")

    print("-------")
count = 0
while True:
    count += 1
    x = int(input("Find number "))

    if x == 41:
     print(f"you found number in {count} steps ")
     break
    else:
        print("Wrong, please find again! ")