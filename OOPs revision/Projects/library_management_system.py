'''
Project 1: Simple Library Management System 
Objective: Develop an OOP-based system to manage books and users in a library. 

Concepts to Apply: 

Classes & Objects: Book, User, Library. 

Attributes & Methods: Store book details (title, author, ISBN, availability), user details (name, user ID, borrowed books), 
and library collection. Methods for borrowing, returning, adding/removing books, registering/unregistering users. 

Encapsulation: Make book_id, user_id, and is_available private/protected where appropriate, with public methods for access and modification. 

Inheritance (Optional but Recommended): 
User base class, with subclasses Librarian and Member. Librarian might have additional methods like add_book() or remove_book(). 
Book base class, with subclasses FictionBook and NonFictionBook, potentially having unique attributes or methods. 

Polymorphism (Optional): If you implement different User types, you could have a perform_action() method that behaves differently based on the user 
type (e.g., Librarian can add_book, Member can borrow_book). 

Core Features: 
Book Management: Add new books, remove existing books, search for books by title/author/ISBN.

User Management: Register new users, remove users. 

Borrowing & Returning: Allow users to borrow books (if available) and return them. 

Tracking: Keep track of which books are borrowed by which user. 

User Interface: Simple text-based menu interface for interaction. 
'''

class Book:
    Book_count = 5
    def __init__(self, title, book_id,author,ISBN, is_available):
        self.__book_id = book_id
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self._is_available = is_available

    def get_book_id(self):
        return self.__book_id
    
    def check_availability(self):
        return self._is_available
    
    def set_availability(self,value):
        self._is_available == value


#user class
class User:
    userCount = 1
    def __init__(self, user_id, name, borrowed_books):
        self.name = name
        self.__user_id = user_id
        self.borrowed_books = list(borrowed_books)

    def get_user_id(self):
        return self.__user_id
    
    def borrow_book(self, book_id):
        pass

    def return_book(self, book_id):
        pass

    def showed_borrowed_books(self):
        pass

# member class
class Member(User):
    def __init__(self, user_id, name, borrowed_books):
        super().__init__(user_id, name, borrowed_books)
        self.designation = "member"

    def borrow_book(self, book_id):
        selected_book = 0
        for book in Library.books:
            if Book.get_book_id() == book_id:
                selected_book = book
        self.borrowed_books.append(selected_book)


    def return_book(self, book_id):
        selected_book = 0
        for book in Library.books:
            if Book.get_book_id() == book_id:
                selected_book = book
        self.borrowed_books.remove(selected_book)
    

    def showed_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"Book: {book.title} borrowed by user : {self.get_user_id()}")


# Librarian class
class Librarian(User):
    def __init__(self, user_id, name, borrowed_books):
        super().__init__(user_id, name, borrowed_books)
        self.designation = "Librarian"
    
    def add_book(self,title, author, ISBN, is_available):
        print("\n-------------------------------------")
        print("creating New Book......")
        print("---------------------------------------")
        Book.Book_count +=1
        new_book = Book(Book.Book_count, title, author , ISBN, is_available)
        Library.books.apends(new_book)
        
        
    def remove_book(self):
        Library.display_books()
        book_id = int(input("Which book you want to remove, Enter Book ID: "))
        
        for book in Library.books:
            if book.get_book_id() == book_id:
                Library.books.remove(book)
                print(f"book: \"{book.title}\" has removed")
                

#library class
class Library:
    def __init__(self, users, books):
        self.users = list(users)
        self.books = list(books)
    def display_books(self):
        print("\Books : ")
        for book in self.books:
            if book.check_availability():
                print(f"{book.get_book_id()}, \"{book.title}\", By  \"{book.author}\"")
            
            
    def display_user(self):
        print("Users: ")
        for user in self.users:
            print(f"{user.get_user_id()},  {user.name}")

    def register_user(self, user):
        print("\n----------------------------")
        print("Creating New User--------------")
        print("-------------------------------")
        User.userCount +=1
        new_user = Member(User.userCount, name, [])
        self.users.append(new_user)

    def unregister_user(self, user_id):
        self.display_user()
        # user_id = input(int("Enter user ID to remove: "))
        
        for user in self.users:
            if user.get_user_id() == user_id:
                self.users.remove(user)
                print(f"User \"{user.name}\" removed successfully")

    def search_book(self):
        option = int(input("what thing you want to search by: \n1 title: \n2 author: \n3 ISBN: "))
        keyword = input("Enter you option: ")
        
        found = False
        match option:
            
            case 1:
                for books in self.books:
                    if keyword == books.title.lower():
                        print(f"{books.get_book_id()}: \"{books.title}\": by \"{books.author}\"")
                        found = True
            case 2:
                for books in self.books:
                    if keyword == books.author.lower():
                        print(f"{books.get_book_id()}: \"{books.title}\": by \"{books.author}\"")
                        found = True
            case 1:
                for books in self.books:
                    if keyword == books.ISBN.lower():
                        print(f"{books.get_book_id()}: \"{books.title}\": by \"{books.author}\"")
                        found = True
            case _:
                print("Invalid choice")
            
        if not found:
            print("Book not found")
            
#main loop starts here

b1 = Book(1, "7 Habits Of Successful People", "Stephen Covey", 2001, bool(1))
b2 = Book(2, "Ego is the Enemy", "Ryan Holiday", 2002, bool(1))
b3 = Book(3, "Harry Potter and the Phiosophers Stone", "J. K. Rowling", 2003, bool(1))
b4 = Book(4, "Harry Potter and the Deathly Hallows", "J. K. Rowling", 2004, bool(1))
b5 = Book(5, "To Kill a Mockingbird", "Harper Lee", 2005, bool(1))
books = [b1,b2,b3,b4,b5] 


user1 = Member(1, "azhar", [])
user2 = Librarian(2, "faizan", [])
users = [user1, user2]



library = Library(users, books)


print("------------------------------")
print("Welcome to Library system")
print("------------------------------")

restart = 1
main_loop = 1

while(main_loop):
    #current_user = int(input("Enter your user id to continue: "))
    
    restart = 1
    while(restart):
        print("\n1. Add User\n2. Remove User" \
        "\n3. Add Book\n4. Remove Book \n" \
        "5. Borrow Book \n6. Return Book \n" \
        "7. Show Borrowed Books \n8. Search a Book" \
        "\n9. Logout\n0. Exit\n11 show all users\n\nEnter your choice:")
        option = int(input())
        match option:
            case 0:
                restart = 0
                main_loop = 0
            
            case 1:
                name = input("Enter user name: ")
                library.register_user(name)

                
            case 2:
                user_id = int(input("input user to ID to remove: "))
                library.unregister_user(user_id)
            
            case 3:
                title = input("Enter titla of new book: ")
                author = input("Enter author of the new book: ")
                ISBN = input("input ISBN : ")
                is_available = True
                user2.add_book(title, author, ISBN, is_available)
            
            case 4:
                user2.remove_book()
            
            case 5:
                book_id = int(input("Enter Book ID to remove: "))
                user2.remove_book(book_id)
            case 6:
                book_id = int(input("Enter returning Book ID :"))
                Member.return_book(book_id)
            case 7:
                user1.showed_borrowed_books()
            case 8:
                library.search_book()
            case 9:
                restart = 0
            case 11:
                library.display_user()
            case _:
                print("\n Invalid input")
                        
                
