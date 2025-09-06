'''
Project 2: Simple E-commerce System Till 11 pm today
Objective: Create an OOP system to simulate a basic online store, allowing customers to browse products, add them to a shopping cart, and place orders. 

Concepts to Apply: 

Classes & Objects: Product, Customer, ShoppingCart, Order. 

Attributes & Methods: 
Product: Name, price, stock quantity. Methods to check availability, reduce stock. 

Customer: Name, customer ID, contact info. 

ShoppingCart: Stores Product objects and quantities. Methods to add/remove items, calculate total. 

Order: Stores ordered items, total amount, customer info, order status. 


Encapsulation: Make product_id, customer_id, stock_quantity, and order_id private/protected, with public getters/setters or methods for interaction. 

Inheritance (Optional but Recommended): 
Product base class, with subclasses ElectronicProduct (might have warranty info) and ClothingProduct (might have size/color). 

Polymorphism (Optional): If different Product types, a display_details() method could show different info based on the product type. 

Core Features: 
Product Catalog: Add products to the store's catalog. 

Shopping Cart: Customers can add products to their cart, update quantities, remove items. 

Checkout Process: Calculate total cost, simulate placing an order. 

Order Tracking: Basic order status (e.g., "Pending", "Shipped"). 

User Interface: Simple text-based menu for customers to interact. 
'''

class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.__stock_quantity = stock_quantity
        
    def get_product_id(self):
        return self.__product_id
    
    def get_stock_quantity(self):
        return self.__stock_quantity
    
    def set_stock_quantity(self, quantity):
        if quantity >= 0:
            self.__stock_quantity = quantity
        else:
            print("Stock quantity cannot be negative")
    
    def check_availability(self, requested_quantity=1):
        return self.__stock_quantity >= requested_quantity
    
    def reduce_stock(self, quantity):
        if self.check_availability(quantity):
            self.__stock_quantity -= quantity
            return True
        else:
            print(f"Insufficient stock. Available: {self.__stock_quantity}, Requested: {quantity}")
            return False
    
    def display_details(self):
        return f"Product ID: {self.__product_id}, Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.__stock_quantity}"


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, warranty_period):
        super().__init__(product_id, name, price, stock_quantity)
        self.warranty_period = warranty_period
    
    def display_details(self):
        base_info = super().display_details()
        return f"{base_info}, Warranty: {self.warranty_period} months"


class ClothingProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, size, color):
        super().__init__(product_id, name, price, stock_quantity)
        self.size = size
        self.color = color
    
    def display_details(self):
        base_info = super().display_details()
        return f"{base_info}, Size: {self.size}, Color: {self.color}"


class Customer:
    def __init__(self, customer_id, name, contact_info):
        self.__customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
    
    def get_customer_id(self):
        return self.__customer_id
    
    def display_info(self):
        return f"Customer ID: {self.__customer_id}, Name: {self.name}, Contact: {self.contact_info}"


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary: {product_id: {'product': product_obj, 'quantity': int}}
    
    def add_item(self, product, quantity=1):
        product_id = product.get_product_id()
        if product.check_availability(quantity):
            if product_id in self.items:
                self.items[product_id]['quantity'] += quantity
            else:
                self.items[product_id] = {'product': product, 'quantity': quantity}
            print(f"Added {quantity} x {product.name} to cart")
            return True
        else:
            print(f"Cannot add {quantity} x {product.name} - insufficient stock")
            return False
    
    def remove_item(self, product_id, quantity=None):
        if product_id in self.items:
            if quantity is None or quantity >= self.items[product_id]['quantity']:
                removed_item = self.items.pop(product_id)
                print(f"Removed all {removed_item['product'].name} from cart")
            else:
                self.items[product_id]['quantity'] -= quantity
                print(f"Removed {quantity} x {self.items[product_id]['product'].name} from cart")
        else:
            print("Item not found in cart")
    
    def update_quantity(self, product_id, new_quantity):
        if product_id in self.items:
            if new_quantity <= 0:
                self.remove_item(product_id)
            else:
                product = self.items[product_id]['product']
                if product.check_availability(new_quantity):
                    self.items[product_id]['quantity'] = new_quantity
                    print(f"Updated quantity to {new_quantity}")
                else:
                    print("Insufficient stock for requested quantity")
        else:
            print("Item not found in cart")
    
    def calculate_total(self):
        total = 0
        for item_info in self.items.values():
            total += item_info['product'].price * item_info['quantity']
        return total
    
    def display_cart(self):
        if not self.items:
            print("Cart is empty")
            return
        
        print("\n--- Shopping Cart ---")
        for item_info in self.items.values():
            product = item_info['product']
            quantity = item_info['quantity']
            subtotal = product.price * quantity
            print(f"{product.name} - Quantity: {quantity}, Price: ${product.price:.2f}, Subtotal: ${subtotal:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
    
    def clear_cart(self):
        self.items.clear()
        print("Cart cleared")


class Order:
    _order_counter = 1
    
    def __init__(self, customer, cart_items):
        self.__order_id = Order._order_counter
        Order._order_counter += 1
        self.customer = customer
        self.ordered_items = dict(cart_items)  # Copy of cart items
        self.total_amount = self._calculate_total()
        self.__order_status = "Pending"
    
    def get_order_id(self):
        return self.__order_id
    
    def get_order_status(self):
        return self.__order_status
    
    def set_order_status(self, status):
        valid_statuses = ["Pending", "Confirmed", "Shipped", "Delivered", "Cancelled"]
        if status in valid_statuses:
            self.__order_status = status
            print(f"Order status updated to: {status}")
        else:
            print(f"Invalid status. Valid options: {valid_statuses}")
    
    def _calculate_total(self):
        total = 0
        for item_info in self.ordered_items.values():
            total += item_info['product'].price * item_info['quantity']
        return total
    
    def display_order(self):
        print(f"\n--- Order #{self.__order_id} ---")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.__order_status}")
        print("Ordered Items:")
        for item_info in self.ordered_items.values():
            product = item_info['product']
            quantity = item_info['quantity']
            subtotal = product.price * quantity
            print(f"  {product.name} - Quantity: {quantity}, Price: ${product.price:.2f}, Subtotal: ${subtotal:.2f}")
        print(f"Total Amount: ${self.total_amount:.2f}")


class Store:
    def __init__(self):
        self.catalog = {}  # Dictionary: {product_id: product_obj}
        self.customers = {}  # Dictionary: {customer_id: customer_obj}
        self.orders = {}  # Dictionary: {order_id: order_obj}
    
    def add_product(self, product):
        self.catalog[product.get_product_id()] = product
        print(f"Added product: {product.name}")
    
    def remove_product(self, product_id):
        if product_id in self.catalog:
            removed_product = self.catalog.pop(product_id)
            print(f"Removed product: {removed_product.name}")
        else:
            print("Product not found")
    
    def find_product(self, product_id):
        return self.catalog.get(product_id)
    
    def display_catalog(self):
        if not self.catalog:
            print("No products available")
            return
        
        print("\n--- Product Catalog ---")
        for product in self.catalog.values():
            print(product.display_details())
    
    def register_customer(self, customer):
        self.customers[customer.get_customer_id()] = customer
        print(f"Registered customer: {customer.name}")
    
    def find_customer(self, customer_id):
        return self.customers.get(customer_id)
    
    def place_order(self, customer, cart):
        if not cart.items:
            print("Cannot place order - cart is empty")
            return None
        
        # Check stock availability for all items
        for item_info in cart.items.values():
            product = item_info['product']
            quantity = item_info['quantity']
            if not product.check_availability(quantity):
                print(f"Order failed - insufficient stock for {product.name}")
                return None
        
        # Reduce stock for all items
        for item_info in cart.items.values():
            product = item_info['product']
            quantity = item_info['quantity']
            product.reduce_stock(quantity)
        
        # Create order
        order = Order(customer, cart.items)
        self.orders[order.get_order_id()] = order
        cart.clear_cart()
        print(f"Order #{order.get_order_id()} placed successfully!")
        return order
    
    def find_order(self, order_id):
        return self.orders.get(order_id)


# Example usage and simple text-based interface
def main():
    store = Store()
    
    # Add sample products
    laptop = ElectronicProduct(1, "Gaming Laptop", 1299.99, 10, 24)
    headphones = ElectronicProduct(2, "Wireless Headphones", 199.99, 25, 12)
    tshirt = ClothingProduct(3, "Cotton T-Shirt", 29.99, 50, "L", "Blue")
    jeans = ClothingProduct(4, "Denim Jeans", 79.99, 30, "M", "Black")
    
    store.add_product(laptop)
    store.add_product(headphones)
    store.add_product(tshirt)
    store.add_product(jeans)
    
    # Register sample customer
    customer = Customer(1, "John Doe", "john@email.com")
    store.register_customer(customer)
    
    # Create shopping cart
    cart = ShoppingCart()
    
    while True:
        print("\n=== E-Commerce Store ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Update Cart Quantity")
        print("6. Checkout")
        print("7. View Orders")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            store.display_catalog()
        
        elif choice == '2':
            store.display_catalog()
            try:
                product_id = int(input("Enter product ID to add: "))
                quantity = int(input("Enter quantity: "))
                product = store.find_product(product_id)
                if product:
                    cart.add_item(product, quantity)
                else:
                    print("Product not found")
            except ValueError:
                print("Please enter valid numbers")
        
        elif choice == '3':
            cart.display_cart()
        
        elif choice == '4':
            cart.display_cart()
            try:
                product_id = int(input("Enter product ID to remove: "))
                cart.remove_item(product_id)
            except ValueError:
                print("Please enter a valid product ID")
        
        elif choice == '5':
            cart.display_cart()
            try:
                product_id = int(input("Enter product ID to update: "))
                quantity = int(input("Enter new quantity: "))
                cart.update_quantity(product_id, quantity)
            except ValueError:
                print("Please enter valid numbers")
        
        elif choice == '6':
            cart.display_cart()
            if cart.items:
                confirm = input("Confirm order? (y/n): ")
                if confirm.lower() == 'y':
                    order = store.place_order(customer, cart)
                    if order:
                        order.display_order()
            else:
                print("Cart is empty")
        
        elif choice == '7':
            if store.orders:
                for order in store.orders.values():
                    order.display_order()
            else:
                print("No orders found")
        
        elif choice == '8':
            print("Thank you for shopping with us!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
        

    