'''
Question 1.1: Define a Python class named Dog. Inside the class, simply use pass. Then, create an instance of this Dog class and assign it to a variable named my_dog. Print the my_dog variable. 
'''
class Dog:
    pass
my_dog = Dog()
print(my_dog)
print('-----------------------------------\n')

'''
Question 1.2: Modify the Dog class to include an __init__ method that takes name and breed as parameters. 
Initialize these as instance attributes. Create two Dog objects: one named "Buddy" of "Golden Retriever" breed, 
and another named "Lucy" of "Labrador" breed. Print the name and breed of both dogs.
'''
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")
print(f"Dog 1: Name = {dog1.name}, Breed = {dog1.breed}")
print(f"Dog 2: Name = {dog2.name}, Breed = {dog2.breed}")
print('-----------------------------------\n')


'''
Question 1.3: Create a class Car with an __init__ method that takes make, model, and year. Add a method display_info 
that prints the car's make, model, and year. Create three different Car objects and call display_info for each. 
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)

for car in (car1, car2, car3):
    car.display_info()
print('-----------------------------------\n')