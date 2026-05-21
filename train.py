# O-TASK(PYTHON)

# Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab chiqqan javobni qaytarsin.
# MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45
# Masalani yechish:
# def calculate_summary(arr):
#        summary = 0

#        for ele in arr:
#               if type(ele) == int:
#                      summary += ele

#        return summary


# print(f"The calculate_summary: {calculate_summary([10, "10", {"son": 10}, True, 35])}")





# M-TASK(PYTHON)

# Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
# MASALAN: palindrom_check("dad") return True
# palindrom_check("son") return False

# def palindrom_check(str): 
#        reverse_str = str[::-1]

#        if str == reverse_str:
#               return True
#        else:
#               return False
       

# print(f"palindrom_check: {palindrom_check("dad")}")
# print(f"palindrom_check: {palindrom_check("son")}")





# K-TASK(PYTHON)

# Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
# MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
# masalani yechish
# def find_longest(str):
#        words = str.split()    
#        longest_word = ""

#        for word in words:
#               if len(word) > len(longest_word):
#                      longest_word = word

#        return longest_word
      
 
# print(f"The longest word: {find_longest("I come from Uzbekistan")}")
 
  
  


# I-TASK(PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"
#  masalani yechish
# def get_digits(str):
#     result = ""

#     for num in str:
#         if num.isdigit():
#             result += num

#     return result


# print(f"the numbers: {get_digits("m14i1t")}")


# G-TASK(PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# masalani yechish
# def get_highest_index(arr):
#        max_value = max(arr)
#        return arr.index(max_value)

# print(f"The highest index: {get_highest_index([5, 21, 12, 21, 8])}")
