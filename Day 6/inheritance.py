class Animal:
    def Speak():
        return "Animal is Speaking"
#single inh:
class Dog(Animal):
    def Bark():
        return"Bow..."
#multi inh
class puppy(Dog):
    def puppy_speak():
        return"im puppy"
obj1=Animal
obj2=Dog
obj3=puppy
print(obj1.Speak())
print(obj2.Bark())
print(obj3.puppy_speak())

