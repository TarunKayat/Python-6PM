def fun(obj):
    print(f"{obj.name}")
    obj.speak()

class Dog:
    name = 'Dog'
    def speak(self):
        print("Barking...")

class Cat:
    name = 'cat'
    def speak(self):
        print("Meow")


class Lion:
    name = 'Lion'
    def speak(self):
        print("Roar")

c = Cat()
d = Dog()
l = Lion()
fun(l)