''' Classlar

(1) What is class?
(2) ordinary vs static properties
(3) special methods 
'''

print("========== What is class? =============")
# class => blueprint for object creation
# Class -> obyektlarni yaratish uchun shablon

# class ning tarkibiy structure: state & constructor & method


class Person():
    # state
    message = "class state property"

    # Constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age} years old)")


        # static methodlar:::
    @staticmethod
    def explain():
        print("Class: Static method property executed")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 45)

# Ordinary state property call
name = person1.name
print("name: ", name)


# ordinary method call
person1.introduce()
person2.say_age()


print("========== ordinary vs static properties =============")
# static state bu togridan togri call ni ozi bilan birga kelyapti
new_message = Person.message
print("new_message: ", new_message)

# static methodni call qilish
Person.explain()