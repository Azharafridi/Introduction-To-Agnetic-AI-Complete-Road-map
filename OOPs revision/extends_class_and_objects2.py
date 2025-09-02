'''
Question 2.1: Building on the Car class from Q1.3, add an instance attribute current_speed initialized to 0. 
Add two instance methods: accelerate(speed_increase) that increases current_speed and brake(speed_decrease) 
that decreases current_speed (ensure speed doesn't go below 0). Demonstrate accelerating and braking a car object. 
'''


class Car:
    def __init__(self, make, model, year, current_speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}") 

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        print(f"The car has accelerated. Current speed: {self.current_speed} km/h")
    def brake(self, speed_decrease):
        self.current_speed -= speed_decrease
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"The car has braked. Current speed: {self.current_speed} km/h")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)

for car in (car1, car2, car3):
    car.display_info()
car1.accelerate(50)
car1.brake(20)


print('-----------------------------------\n')

'''
Question 2.2: Create a Student class. Its __init__ method should take name and student_id. Add an instance method enroll_course(course_name) 
which adds the course_name to a list of courses associated with the student. Add another method get_courses() that returns the list of enrolled courses. 
'''
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} has enrolled in {course_name}")

    def get_courses(self):
        return self.courses
    
student1 = Student("Alice", "S123")
student1.enroll_course("Mathematics")
student1.enroll_course("Physics")
print(f"{student1.name} is enrolled in: {student1.get_courses()}")
print('-----------------------------------\n')


'''
Question 2.3: Design a BankAccount class. Its __init__ should take account_number and initial_balance. Include instance methods deposit(amount) and withdraw
(amount). Ensure withdrawals cannot go below zero balance. 
'''

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
acc1 = BankAccount("A123", 100)
acc1.deposit(50)
acc1.withdraw(30)
acc1.withdraw(150)  # Should show insufficient funds
print('-----------------------------------\n')



class Dog:
    number_of_Dogs = 0
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.number_of_Dogs += 1

    @classmethod
    def get_total_Dogs(cls):
        return cls.number_of_Dogs

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")
print(f"Dog 1: Name = {dog1.name}, Breed = {dog1.breed}")
print(f"Dog 2: Name = {dog2.name}, Breed = {dog2.breed}")
dog3 = Dog("Tommy", "Beagle")
dog4 = Dog("Max", "Bulldog")

print(f"Total number of dogs: {Dog.get_total_Dogs()}")
print('-----------------------------------\n')



'''
Question 2.5: Create a Product class. It should have a class attribute discount_rate initialized to 0.10 (10%). The __init__ method should take name and price. 
Add an instance method get_discounted_price() that calculates the price after applying the discount_rate. Add a class method set_discount_rate(new_rate) that 
allows modifying the discount_rate. 
'''

class Product:
    discount_rate = 0.10  # Class attribute for discount rate
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        discounted_price = self.price * (1 - Product.discount_rate)
        return discounted_price
    
    @classmethod
    def set_discount_rate(cls, new_rate):
        cls.discount_rate = new_rate
product1 = Product("Laptop", 1000)
print(f"{product1.name} discounted price: ${product1.get_discounted_price()}")
Product.set_discount_rate(0.25)  # Change discount rate to 15%
print(f"New discounted price: ${product1.get_discounted_price()}")
print('-----------------------------------\n')


'''
Question 2.6: Design a Circle class. Add a class attribute PI set to 3.14159. The __init__ should take radius. 
Add an instance method calculate_area(). Create a class method set_pi_precision(new_pi) that allows changing the value of PI. 
'''

class Circle:
    pi = 3.14159  # Class attribute for pi

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = Circle.pi * (self.radius ** 2)
        return area
    @classmethod
    def set_pi_precision(cls, new_pi):
        cls.pi = new_pi
circle1 = Circle(5)
print(f"Circle with radius {circle1.radius} has area: {circle1.calculate_area()}")
Circle.set_pi_precision(3)  # Change the value of pi
print(f"With new pi value, area: {circle1.calculate_area()}")
print('-----------------------------------\n')


'''
Question 2.7: In the Car class, add a static method display_general_car_safety_tips(). This method should print some 
generic safety advice (e.g., "Always wear seatbelts."). It should not access any instance or class attributes. 
'''

class Car:
    def __init__(self, make, model, year, current_speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}") 

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        print(f"The car has accelerated. Current speed: {self.current_speed} km/h")
    def brake(self, speed_decrease):
        self.current_speed -= speed_decrease
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"The car has braked. Current speed: {self.current_speed} km/h")
    ## adding a static method
    @staticmethod
    def display_general_car_safety_tips():
        print("always wear seatbelt")

car1 = Car("Toyota", "Camry", 2020)
print("this is Car class and is made to extand to static method")
Car.display_general_car_safety_tips()

print('-----------------------------------\n')



'''
Question 2.8: Create a MathUtility class. Add a static method add(a, b) that returns the sum of a and b. Add another static method multiply(a, b). These methods should not depend on the state of any MathUtility object. 
'''

class MathUtility:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

math_util = MathUtility()
print("This is MathUtility class and is made to extand to static method")
print(f"Addition: {math_util.add(5, 3)}")
print(f"Multiplication: {math_util.multiply(5, 3)}")
print('-----------------------------------\n')



'''
Question 2.9: For the Student class, add a static method generate_student_id(). This method should generate a random 
6-digit student ID (e.g., using random module). It should not take self or cls as arguments and should not rely on any 
instance or class data. 
'''

import random
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} has enrolled in {course_name}")

    def get_courses(self):
        return self.courses
  
    @staticmethod
    def generate_student_id():
        return f"S{random.randint(100000, 999999)}"
print("This is Student class and is made to extand to static method")
student1 = Student("Alice", Student.generate_student_id())
print(f"Generated Student ID for {student1.name}: {student1.student_id}")
student1.enroll_course("Mathematics")
