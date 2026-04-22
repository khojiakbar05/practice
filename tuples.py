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

animals[0] = "bird"
print("after tuple_obj: ", tuple_obj)


