class Animal:
    name: object

    def __init__(self, name):
        self.name = name
        self.age = 2

    def speak(self):
        print(self.age)
        print('i am an animal')


class Dog(Animal):
    def speak(self):
        print('i am a dog')


class Bear(Animal):
    def speak(self) -> object:
        print('i am a bear named', self.name)


animal = Animal(name='fluffy')
dog = Dog(name='fido')
bear_1 = Bear(name='baloo')
bear_2 = Bear(name='yogi')
animal.speak()
dog.speak()
bear_1.speak()
bear_2.speak()
