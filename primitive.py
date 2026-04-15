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


