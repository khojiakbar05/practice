''' CLASS DEEP DIVE
       (1) ENCAPSULATION
       (2) INHERITANCE <
       (3) POLYMORRPHISM <
'''

print("========== Inheritance =============")
# Parent > child
# Parent only provides Public & protected properties(state + method) to cild!


class Animal:     # Parent class
    # State
    description = "The class creates animals"

    # Constructure
    def __init__(self, voice):
        self._status = "Animal is Alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"The animal make a voice {self.voice}")


class Dog(Animal):     # Child class
    # state

    # constructure
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")

    def make_voice(self):
        print(f"The {self.name} says:  {self.sound}")


class Cat(Animal):    # Child class
    # state

    # constructure
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):     # Child class
    # state

    # constructure
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can protect you")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("--------")

dog.make_voice()
cat.make_voice()
fish.make_voice()


print("--------")

print("Parent class: ", Animal.description)
print("Child class: ", Dog.description)
print("dog.status: ", dog._status)


print("========== Polymorphism =============")


dog.make_voice()
fish.make_voice()


print("--------")

# fish > fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print("The result: ", {result})

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data: ", data1, data2)

