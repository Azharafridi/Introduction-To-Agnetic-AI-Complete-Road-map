
# Method Overriding (as a form of Polymorphism) 
'''
Question 5.1: (Revisit) Create a base class Shape with a method draw(). Create subclasses Circle and Square, both overriding draw() to print "Drawing a Circle" and "Drawing a Square" respectively. Create a list of Shape objects (containing both Circle and Square instances) and iterate through it, calling draw() on each. 
'''

class Shape:
    def __init__(self):
        pass
    def draw(self):
        print("Drawing a shape")
    
class Circle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        print("Drawing a circle")
class Square(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        print("Drawing a square")

shapes = [Circle(), Square(), Shape(), Circle(), Square()]

for shape in shapes:
    shape.draw()
print('-----------------------------------\n')


'''
Question 5.2: Define a Printer base class with a print_document(doc) method. Create subclasses LaserPrinter and InkjetPrinter. Override print_document in each to simulate different printing behaviors (e.g., "Laser printing..." vs. "Inkjet printing..."). Demonstrate by putting instances in a list and calling the method. 
'''

class Printer:
    def __init__(self):
        pass
    def print_document(self, document):
        print(f"Printing document: {document}")
    

class LaserPrinter(Printer):
    def __init__(self):
        pass

    def print_document(self, document):
        print(f"Laser printing document: {document}")

class InkjetPrinter(Printer):
    def __init__(self):
        pass
    def print_document(self, document):
        print(f"Inkjet printing document: {document}")


printers = [LaserPrinter(), InkjetPrinter(), Printer(), LaserPrinter()]
for printer in printers:
    printer.print_document("printing this document")

print('-----------------------------------\n')


'''
Question 5.3: Create a base class PaymentMethod with a method process_payment(amount). Create subclasses CreditCardPayment, PayPalPayment, and CashPayment. Override process_payment in each to simulate specific payment processing steps. 
'''

class PaymentMethod:
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
    
class CreditCardPayement(PaymentMethod):
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
class PayPalPayment(PaymentMethod):
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
class CashPayement(PaymentMethod):
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing cash payment of ${amount}")

amount = 100
payment_methods = [CreditCardPayement(), PayPalPayment(), CashPayement(), PaymentMethod()]
for method in payment_methods:
    method.process_payment(amount)
print('-----------------------------------\n')


# Polymorphism with a Common Interface (Duck Typing) 
'''
Question 5.4: Create two unrelated classes, Robot with a perform_action() method and Human with a perform_action() method. The Robot's method should print "Robot is performing a task," and the Human's should print "Human is performing an activity." Create a list containing instances of both Robot and Human and call perform_action() on each, demonstrating polymorphism through "duck typing." 
'''

class HumanAction:
    def __init__(self):
        pass
    def perform_action(self):
        print("Human is performing an activity")

class RobotAction:
    def __init__(self):
        pass

    def perform_action(self):
        print("Robot is performing an activity")

actions = [HumanAction(), RobotAction(), RobotAction(), HumanAction()]
for action in actions:
    action.perform_action()
print('-----------------------------------\n')



'''
Question 5.5: Define a function process_items(items_list) that iterates through a list. Each item in the list is expected to have a process() method. Create two distinct classes, FileProcessor and DataAnalyzer, each with a process() method that does something different. Demonstrate process_items working with a list containing instances of both. 
'''

class FileProcessor:
    def __init__(self):
        pass
    def process(self):
        print("File processor:  ")

class DataAnalyzer:
    def __init__(self):
        pass
    def process(self):
        print("Data analyzer:  ")

def process_items(items):
    for item in items:
        item.process()
items = [FileProcessor(), FileProcessor() ,DataAnalyzer(), FileProcessor()]
process_items(items)
print('-----------------------------------\n')


'''
Question 5.6: Create a Notifier function that takes an object and calls its send_notification() method. Then, create two classes EmailSender and SMSSender, both having a send_notification() method (with different implementations). Show how Notifier can work with either. 
'''

class EmailSender:
    def __init__(self):
        pass
    def send_notification(self):
        print("Sending email notification")
    
class SMSSender:
    def __init__(self):
        pass
    def send_notification(self):
        print("Sending SMS notification")

def notifeir(obj):
    for o in obj:
        o.send_notification()

obj = [EmailSender(), SMSSender(), EmailSender(), SMSSender(), SMSSender()]
notifeir(obj)
print("--------------------------------\n")




# Operator Overloading (Briefly) 
'''
Question 5.7: Create a Vector class with x and y coordinates. Override the __add__ operator so that two Vector objects can be added together, 
resulting in a new Vector object where x and y coordinates are summed independently. 
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        return Vector(self.x + obj.x, self.y + obj.y)
    def display(self):
        print(f"Vectors : {self.x},{self.y} \n")
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
v3.display()
print('-----------------------------------\n')


'''
Question 5.8: For the Book class (from Q4.2), override the __len__ method to return the length of the book's title. 
'''

class Book:
    def __init__(self, title, author , isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
    def __len__(self):
        return len(self.title)
book = Book("1984", "George Orwell", "1234567890")
print(f"Length of book title: {len(book)}")
print("----------------------------------\n")     


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, obj):
        if self.amount == obj.amount:
            return True
        else:
            return False

m1 = Money(100)
m2 = Money(200)
if m1 == m2:
    print("Both are equal")
else:
    print("Both are not equal")
print('-----------------------------------\n')