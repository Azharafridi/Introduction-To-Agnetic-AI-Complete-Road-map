'''
Question 3.1: Create a base class Animal with an __init__ taking name and sound. Add a method make_sound() that prints the animal's name and sound. Create a subclass Dog that inherits from Animal. Create an instance of Dog and call make_sound(). 
'''

class Animal:
    def __init__(self, name , sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} sounds is : {self.sound}"
    

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)



puppy = Dog("Tommy", "Bark Bark")
print("Animal class with single inheritance is here : ")
print(puppy.make_sound())
print('-----------------------------------\n')


'''
Question 3.2: Define a base class Shape with a method area() that returns 0. Create two subclasses: Rectangle (with length and width) and Circle (with radius). Both subclasses should override the area() method to calculate their specific area. 
'''

class Shape:

    def area(self):
        return 0
    

class Rectangle(Shape):
    def __init__(self, width, height):
#        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
        def __init__(self, radius):
 #           super().__init__()
            self.radius = radius

        def area(self):
            return  3.14159 * (self.radius ** 2)

shap_obj = Shape()
print('Shape class with method overriding is here : ')
print(f"Area of Shape : {shap_obj.area()}")
reactangle_obj = Rectangle(5, 10)
print(f"Area of Rectangle : {reactangle_obj.area()}")
circle_obj = Circle(7)
print(f"Area of Circle : {circle_obj.area()}")
print('-----------------------------------\n')
  

class Employee():
    def __init__(self, name, employee_id):
        self.name  = name
        self.employee_id = employee_id
        
    def get_details(self):
        print(f"Employee Name : {self.name}, Employee ID : {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)    # TOdo what's memory level happering here??
        self.department = department


manager = Manager("Alice", "M123", "Sales")
print("Employee class with multilevel inheritance is here : ")
manager.get_details()
print('-----------------------------------\n')


'''
Question 3.4: From Q3.1, in the Dog subclass, override the make_sound() method so that instead of just printing "Woof!", it prints "{} says: Woof Woof!". Ensure the Animal's __init__ is still called correctly using super(). 
'''


class Animal:
    def __init__(self, name , sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} sounds is  : {self.sound}"
    

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    def make_sound(self):
        return f"{self.name} says : {self.sound}"
    


animal_obj = Animal("Lion", "Roar")
print("Animal class with single inheritance is here : ")
print(f"this is animal class sounds : {animal_obj.make_sound()}")
puppy = Dog("Tommy", "Bark Bark")
print("Animal class with single inheritance is here : ")
print(puppy.make_sound())
print('-----------------------------------\n')



'''
Question 3.5: Extend the Employee and Manager classes. Override the get_details() method in Manager to also include the department information, while still calling the Employee's get_details() using super(). 
'''


class Employee():
    def __init__(self, name, employee_id):
        self.name  = name
        self.employee_id = employee_id
        
    def get_details(self):
        print(f"Employee Name : {self.name}, Employee ID : {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)    # TOdo what's memory level happering here??
        self.department = department
    def get_details(self):
        super().get_details()
        print("and my dept is : ", self.department)



manager = Manager("Alice", "M123", "Sales")
print("Employee class with multilevel inheritance is here : ")
manager.get_details()
print('-----------------------------------\n')

