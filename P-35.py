# Program to demonstrate single, multilevel and multiple inheritance


# -------- Single Inheritance --------

class Person:
    def person_info(self):
        print("This is the Person class.")


class Student(Person):
    def student_info(self):
        print("This is the Student class.")


print("----- Single Inheritance -----")

student = Student()
student.person_info()
student.student_info()


# -------- Multilevel Inheritance --------

class Animal:
    def animal_info(self):
        print("This is the Animal class.")


class Dog(Animal):
    def dog_info(self):
        print("This is the Dog class.")


class Puppy(Dog):
    def puppy_info(self):
        print("This is the Puppy class.")


print("\n----- Multilevel Inheritance -----")

puppy = Puppy()
puppy.animal_info()
puppy.dog_info()
puppy.puppy_info()


# -------- Multiple Inheritance --------

class Father:
    def father_info(self):
        print("This is the Father class.")


class Mother:
    def mother_info(self):
        print("This is the Mother class.")


class Child(Father, Mother):
    def child_info(self):
        print("This is the Child class.")


print("\n----- Multiple Inheritance -----")

child = Child()
child.father_info()
child.mother_info()
child.child_info()