# Public Members 

'''
Question 4.1: Create a class Person with name and age as public attributes. Create an object, access and modify these attributes directly, and print them to demonstrate public access. 
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 30)
person.display_info()
person.name = "Doe"  # Modifying public attribute
person.age = 31      # Modifying public attribute
print("After modification:")
person.display_info()
print('-----------------------------------\n')


'''
Question 4.2: Design a Book class with public attributes title, author, and isbn. Create a Book object and print its attributes. 
'''

class Book:
    def __init__(self, title, author , isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

book = Book("1984", "George Orwell", "1234567890")
book.display_info()
print("----------------------------------\n")

'''
Question 4.3: Create a class Wallet with a public attribute balance. Add methods add_money(amount) and spend_money(amount) that directly modify balance. 
'''

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        return self.balance

    def spend_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance

wallet = Wallet(100)
print(f"Initial Balance: {wallet.balance}")
wallet.add_money(50)
print(f"Balance after adding money: {wallet.balance}")
wallet.spend_money(30)
print(f"Balance after spending money: {wallet.balance}")
print(wallet.spend_money(150))  # Attempt to spend more than the balance
print('-----------------------------------\n')


# Protected Members (Convention) 

'''
Question 4.4: Modify the Person class to have _address as a protected attribute (using a single leading underscore). Show that it can still be accessed directly but explain why this is discouraged. Add a public method get_address() to access it. 
'''

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self._address = address  # Protected attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def get_address(self):
        return self._address

person1 = Person("Alice", 28, "islamabad")
print(person1.get_address())  # Accessing protected attribute via method
print(person1._address)  # Accessing protected attribute directly (not recommended)
person1._address = "peshawar"  # Modifying protected attribute directly (not recommended)
print(person1.get_address())
print('-----------------------------------\n')


'''
Question 4.5: For the BankAccount class, change account_number to _account_number to indicate it's protected. Add a public method get_account_number() to safely retrieve it. 
'''

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  # Protected attribute
        self.initial_balance = initial_balance


    def get_account_number(self):
        return self._account_number
acc1 = BankAccount("123456789", 1000)
print(f"Account Number: {acc1.get_account_number()}")
print("-----------------------------------\n")


'''
Question 4.6: Create a Configuration class that stores settings. Make a setting like _database_url protected. Explain that while Python doesn't strictly enforce protection, it's a signal for developers. 
'''

class Configuration:
    def __init__(self, database_url):
        self._database_url = database_url  # Protected attribute

    def get_database_url(self):
        return self._database_url
    
c1 = Configuration("https:dasfdealksdjf")
print(c1.get_database_url())



class Person:
    def __init__(self, name, age, address, ssn):
        self.name = name
        self.age = age
        self._address = address  # Protected attribute
        self.__ssn = ssn  # Private attribute

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def __get__ssn(self):
        print(f"my ssn is {self.__ssn}")
    
    def GETGET(self):
        self.__get__ssn()
    
person1 = Person("Alice", 28, "islamabad", "123-45-6789")
person1.set_ssn("987-65-4321")

# print(person1.__ssn)  # This will raise an AttributeError
#person1.__get__ssn()  # Accessing private method via name mangling  # This will raise an AttributeError
person1.GETGET()
print('-----------------------------------\n')


'''
Question 4.8: In the BankAccount class, make __balance truly private. Implement deposit() and withdraw() methods to be the only ways to modify the balance. Add a get_balance() method. 
'''

class BankAccount:
    def __init__(self, account_number,balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        print(f"current balance is : {self.__balance}")

acc1 = BankAccount("123456789", 1000)
acc1.deposit(500)
print(acc1.withdraw(200))
acc1.get_balance()
print('-----------------------------------\n')


'''
Question 4.9: Design a LoginSystem class. Make __password_hash a private attribute. 
Implement a set_password(password) method that hashes the password before storing and a 
verify_password(password) method that checks against the stored hash. 
'''

class LogSystem:
    def __init__(self, password_hash):
        self.__password_hash = password_hash


    def set_password(self, password_hash):
        self.__password_hash = password_hash
    
    def verify_password(self, password_hash):
        if self.__password_hash == password_hash:
            return 1
        else:
            return 0
        

print("LoginSystem class with private members is here : ")
system = LogSystem("hashed_password_123")
if system.verify_password("hashed_password_123"):
    print("/n Access Granted")
else:
    print("Wrong Password")
print('-----------------------------------\n')

