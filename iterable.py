print("========== Iterable Objects =============")
# Iterable objects: => string, dict, tuple, list, range, map, filter
# Iterable => takrorlasnish xususiyati

range_obj = range(3)
print("range_obj: ", range_obj)


text = "MIT"
for letter in text:
    print(f"The letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")


print("========== DICTIONARY =============")
# DICTIONARY is Json Object!.

person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single="True")  # Keyword => argument
print(f"The person: {person}")
print(f"The person1: {person_obj}")

# dctionaryni ichidagi propertylar ni qolga olish
name = person_obj["name"]
print("name: ", name)
age = person["age"]
print("age: ", age)

# name = person_obj["xobby"]
# print("name: ", name)
# dictionaryni ichida yoq bolgan keyni tanlasak xatolik beradi

# nethod: get()
name = person_obj.get("name")
hobby = person_obj.get("xobby")
balance = person_obj.get("balance", 0)

print(f"the name: {name}, hobby: {hobby}, balance is: {balance}")


for key in person_obj:
    print(f"the key: {key}")


# person_obj ichidan single degan keyni ocirib tashlash
del person_obj["single"]
for key in person_obj:
   
    # person_obj ichidan keylarni valuesini olish
    print(f"The key after deleting: {key} => value {person_obj[key]}")
    print(f"the key after del get(): {key} => value {person_obj.get(key)}") 
