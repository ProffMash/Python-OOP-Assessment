class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

# Dog class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# instance of Dog
my_dog = Dog()

# Calling methods from the Animal class
my_dog.eat()    # Inherited method
my_dog.sleep()  # Inherited method

# Calling the method from the Dog class
my_dog.bark()   # Dog's specific method
