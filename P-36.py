# Program to demonstrate method overriding and polymorphism

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    # Method overriding
    def sound(self):
        print("Dog barks")


class Cat(Animal):

    # Method overriding
    def sound(self):
        print("Cat meows")


# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
print("Animal:")
animal.sound()

print("\nDog:")
dog.sound()

print("\nCat:")
cat.sound()