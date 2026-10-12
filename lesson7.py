#OOPS 

#class student:
#    def __init__(self, name, gpa):
#        self.name = name
#        self.gpa = gpa

#    def introduce(self):
#        print("Hi, my name is", self.name, "and my GPA is", self.gpa)

#student1 = student("Alice", 3.8)   
#student2 = student("Bob", 3.5)
#student3 = student("Charlie", 3.9)       
#student1.introduce()
#student2.introduce()
#student3.introduce()

#class Dog:
 #   def __init__(self, name, breed):
  #      self.name = name
   #     self.breed = breed

    #def bark(self):
     #   print(self.name, "says: Woof!")

    #def describe(self):
     #   print("my name is", self.name, "and I am a", self.breed)

#my_dog = Dog("Bruno", "Labrador")
#my_dog.bark()
#print(my_dog.name)
#print(my_dog.breed)
#my_dog.describe()

#class Car:
#    def __init__(self, brand, speed):
#        self.brand = brand
#        self.speed = speed

#    def drive(self):
#        print("the", self.brand, "is driving at", self.speed, "mph")

#car_1 = Car("Mitsubishi", 50)
#car_2 = Car("Toyota", 60)
#car_1.drive()
#car_2.drive()

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

class Dog(Animal):
    def bark(self):
        print(self.name, "says: Woof!")

my_dog = Dog("Bruno")
my_dog.eat()
my_dog.bark()