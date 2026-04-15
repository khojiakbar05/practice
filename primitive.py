print("======= Numbers ========")

# In JAVA & C & JS, -> variables malumot manzilini nomlanishi
# In Python,        -> variables referenceni nomlanishi

# primitive variables -> numbers, strings, booleans => bular OBJECT hammasi

count = 100
count_type = type(count)  # typeni bilish
print("count: ", count, count_type)
# print("count: ", count)

print(f"the count: {count} and type: {count_type}")
# f -> bu super stringga oxshaydi formatlash uchun ishlatiladi

result1 = count.bit_count()  # method
result2 = count.numerator  # state

print("result1: ", result1)
print("result2: ", result2)


print("======= strings ========")

'''
                     METHODS most used => 

upper() -> hamma harflarni katta qiladi
lower() -> hamma harflarni kichik qiladi
title() -> hamma sozlarni bosh harfini katta qiladi
find() -> string ichida qidirish uchun ishlatiladi
replace() -> string ichidagi biror narsani boshqasi bilan almashtirish uchun ishl

'''

# course = "AI Python Fullstack"
# result = type(course)
# print(f"the typee of course: {result}")

# result = course.title() # title() -> method hamma sozlarnoi bosh harfini katta qilib beradi
# print("the result of title: ", result)

# result = course.upper() # upper() -> method hamma harflarni katta qilib beradi
# print("the result of upper: ", result)

# result = course.lower()  # lower() -> method hamma harflarni kichik qilib beradi
# print("the result of lower: ", result)


# replace() -. methodi in use

course = "AI Python Fullstack"
result = type(course)
print(f"The result (1): {result}")

result = course.title()
print(f"The result (2): {result}")

result = course.replace("Fullstack", "MasterClass")
print(f"The result (3): {result}")

print(course)


print("======= boolean ========")

# Builtin => functions => type(), input(), bool(), int(), str()

# type() -> bu funksiya malumot turini bilish uchun ishlatiladi
# input() -> bu funksiya foydalanuvchidan malumot olish uchun ishlatiladi
# bool() -> bu funksiya malumot turini boolean ga o'zgartirish uchun ishlatiladi
# int() -> bu funksiya malumot turini integer ga o'zgartirish uchun ishlatiladi
# str() -> bu funksiya malumot turini string ga o'zgartirish uchun ishlatiladi

y = input("Give your value for y: ")
print("y: ", y)


result = y.isnumeric()
print(f"the input is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY > True => true, 1, " ", [1,2], {"key": "value"}, (1,2), 
# FALSY > False => false, 0, "", [], {}, None

test_falsy = "" or False or None
print("The Falsy value: ", bool(test_falsy))

test_truthy = "hello"
print("The Truthy value: ", bool(test_truthy))
