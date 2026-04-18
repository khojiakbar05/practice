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


print("========== special/magic methods =============")
# Pythons most common special methods are below:
# __init__, __new__, __str__, __call__, __getitem__, __eq__, __len__....


class Car():
    # State
    description = "This classs makes cars"

    # Constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"{self.name} start engine")

    def stop_engine(self):
        print(f"{self.name} stop engine")

    def __str__(self):
       return f"{self.name} was produced {self.year}"
    
    def __call__(self):
        print("Object called like function!!!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()


print("-----")
your_car = Car("Toyota", 2026)
print(your_car)

response = your_car() # Functionga oxshab ishga tushurish
print("response: ", response)
