''' OPERATORS & CONDITIONS
       (1) Operators
       (2) Conditions
       (3) Logical Operators
'''

print("========== Opertors ===========")
# Operators =>  +, -, >,>=, <, <=, *, /, is,   //, %, +=, **
  
a = 19
b = 5

# print("a > b: ", a > b)
# print("a * b: ", a * b)
# print("a / b: ", a / b)

result = a // b
left = a % b
print(f"The result: {result} and left: {left}")

# a = a + 100
a += 100
print("a: ", a)


print("b*b: ", b**2)
print("b*b*b: ", b**3)


print("="*6)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c

print("c == d: ", c == d) # only value
# pythonda faqat VALUE solishtiriladi reference emas

print(id(c), id(d))

data = c is d   # is operatori referencini tekshirish uchun ishlatiladi 
print("c is d: ", c is d) # referencini tekshirish.  False

print("c is e: ", c is e) # True
print(id(c), id(e))