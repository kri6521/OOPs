# simple inheritance
"""
# base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


# derived class
class Dog(Animal):
    def __init__(self):
        self.behaviour = "friendly"

    def speak(self):
        print(f"{self.name} barks, He is very {self.behaviour}")


animal = Animal("generic")
animal.speak()

dog = Dog("buddy")
dog.speak()
"""


# super keyword
class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound")


# derived class
class Dog(Animal):
    # when we wnat upr constructor ka b attribute rkhna n niche wale ko b additional define hojaye
    def __init__(self, breed):
        super().__init__()  # super func lgakr uss method ko mention jo parent s inherit krna h
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks, He is very {self.breed}")


dog = Dog("golden")
dog.speak()
