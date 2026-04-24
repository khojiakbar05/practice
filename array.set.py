''' Array & Set
       (1) Array
       (2) Set
       (3) Specific operators with set
'''

print("========= Array ============")
# Array maxsus vaziyatlarda ishlatiladi yani juda ham katta hajmga ega bolgan raqamlar va qiymatlar bilan ishlanadi
# qolgan oddiy holatlarda listni ozidan foydalanamiz

# pythonda arrayda stricy type hisoblanadi yani ichida faqat numbers yoki faqat string qabul qiladi
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
