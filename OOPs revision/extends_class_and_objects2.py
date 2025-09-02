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
car1.brake(40)

print('-----------------------------------\n')