''' Array & Set
       (1) Array
       (2) Set
       (3) Specific operators with set
'''

print("=========== Array ============")
# Array maxsus vaziyatlarda ishlatiladi yani juda ham katta hajmga ega bolgan raqamlar va qiymatlar bilan ishlanadi
# qolgan oddiy holatlarda listni ozidan foydalanamiz

# pythonda arrayda strict  type hisoblanadi yani ichida faqat numbers yoki faqat string qabul qiladi
from array import array

numbers = array("i", [1, 4, 5, 7, 8, 41])

print("numbers(1): ", numbers)
numbers.append(100)
numbers.insert(0, 14)
print("numbers(2): ", numbers)


numbers.remove(5)
numbers.pop()
print("numbers(3): ", numbers)

del numbers[0:2]
print("numbers(4): ", numbers)
 

print("=========== Set ============")
# { SET } unique collection without keeping order

# SET list va arraydagi sonlarimizdagii bir xillarini bitta deb qabul qiladi va bu setda Index tushunchasi bolmaydi
new_numbers = array("i", [1, 4, 5, 4, 5, 7, 7, 8, 41])
numbs_set = set(new_numbers)

print(f"the number_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1): ", numbs_set)

numbs_set.add(7)
print("numbs_set(2): ", numbs_set)


print("=========== Specific operators with set ============")
#   | , & , - , ^


a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union.   => a va b toplamdagi qiymatlarni unique bolgan raqamlarni olib beradi
result2 = a & b  # intersection => a va b da bor bolgan qymatlarni beradi
result3 = a - b  # difference => ikkalasida bir xil bolgan qiymatlarni ayrib tashlaydi va a ni qolgan qiymatlarini qaytaradyi 
result4 = a ^ b  # symetric difference => bir birida qatnashmagan qiymatlarni qaytaradi



print("result(1): ", result1)
print("result(2): ", result2)
print("result(3): ", result3)
print("result(4): ", result4)


