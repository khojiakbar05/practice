print("======= Numbers ========")

# In JAVA & C & JS, -> variables malumot manzilini nomlanishi
# In Python,        -> variables referenceni nomlanishi

# primitive variables -> numbers, strings, booleans => bular OBJECT hammasi

count = 100
count_type = type(count) # typeni bilish
print("count: ", count, count_type)
# print("count: ", count)

print(f"the count: {count} and type: {count_type}")
# f -> bu super stringga oxshaydi formatlash uchun ishlatiladi
 
result1 = count.bit_count() # method
result2 = count.numerator # state

print("result1: ", result1)
print("result2: ", result2)



