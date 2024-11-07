class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

# polymorphism
def animal_sound(animal):
    animal.make_sound()

# instances of Cat and Dog
my_cat = Cat()
my_dog = Dog()

# Demonstrate polymorphism by passing both Cat and Dog instances
animal_sound(my_cat)  # Output: Meow
animal_sound(my_dog)  # Output: Woof
