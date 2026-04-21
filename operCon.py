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

print("c == d: ", c == d)  # only value
# pythonda faqat VALUE solishtiriladi reference emas

print(id(c), id(d))

data = c is d   # is operatori referencini tekshirish uchun ishlatiladi
print("c is d: ", c is d)  # referencini tekshirish.  False

print("c is e: ", c is e)  # True
print(id(c), id(e))


print("========== Conditions =========")
# Conditionlkar faqat TRUETHY hamda FALSY qiymatlarimizni tekshiradi
x = 89

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("---------")


print("========== Ternery Operators =========")

age = 12
# person = None

# if age > 16:
#        person = "Adult"
# else:
#        person = "Child"

# print("person: ", person)


# Ternery Operartor
person = "adult" if age > 18 else "minor"
print("person: ", person)

print("--------")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("Welcome here, do you want to be a student!")
elif is_admin:
    print("Please, go to this office!")
    # elif is_guest or is_parent
elif is_guest or is_parent:
    print("waiting room is over there!")
else:
    print("other cases")

# or (yoki) True qiymatlarni oladi
# and (va) False qiymatlarni oladi
