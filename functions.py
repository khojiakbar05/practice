'''
Functions
(1) Define vs Call
(2) Parameters vs Arguments
(3) Keyword & Default arguments
(4) scopes
'''

print('======= Define vs Call  =========')

# build in funcion => print(), type()
# function => reusable code of block
# instead  of block {} in Java, Python uses indentation!

# indentation => kodning mantiqiy bloklarini ajratish uchun ishlatiladigan majburiy qoidadir.

# Pythonda ham qiymat qaytarish boyicha ikkiga bolinadi: Return & Void functions
# Void function pythonda : none qqaytaradi
# Jsda void function => Undefined qaytaradi

# define => (parameters) functionni qurish


def greet(a):                      # bu VOID function, chunki hech narsa qaytarmaydi
    print(f"How do you do, {a}")


def greeting(b):                   # bu RETURN function, chunki string qaytaradi
    print("greeting ix executed")
    return f"Hi {b}"


# call => (arguments) functionni chaqirish
result1 = greet("Alice")
print("result1: ", result1)

result2 = greeting("Justin")
print("result2: ", result2)

#(2) Parameters vs Arguments


 


