# email = input("Enter your email: ")

# if email.find("@") != -1:
#        print("The email is valid")
# else:
#        print("The email is not valid")


# age = input("Enter your age: ")
# if age.isdigit():
#        print("The age is valid")
# else:
#        print("The age is NOT valid!!!")


# list1 = ["apple", "banana", "cherry", 12, "true", 0]
# print("list: ", list1[len(list1)-1])


i = 100
while (i <= 200):
    print(i)
    i += 20

a = "my name is khoji"
result = a.capitalize()
print(result)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 7, 8, 9}

print(s1 & s2)


income = 500
if income > 2500:
    tax = 500
else:
    tax = 200
    print("income ", tax)





name = input("What is your name: ")
age = int(input("How old are you: "))
year = 2005 - age + 100

print(name + ", you will be 100 years old in the year " + str(year))
