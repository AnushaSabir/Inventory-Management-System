Inventory Management System – Project Summary
The Inventory Management System is a console-based Python application that simplifies the management of different types of products in a store. It enables the user to add, sell, search, and remove products, while maintaining stock levels accurately. The system is developed using core Object-Oriented Programming (OOP) concepts for better code modularity, reusability, and maintainability.

System Architecture and Mechanism
1. Product Hierarchy (Abstraction & Inheritance)
At the heart of the system is the abstract base class Product, which defines the common structure and behavior of all products. It includes:

Attributes:

product_id

name

price

quantity_in_stock

Shared Methods:

restock(amount)

sell(quantity)

get_total_value()

__str__() (to print product details)

Three specialized product types inherit from Product:
Electronics: Adds warranty_years, brand

Grocery: Adds expiry_date, method is_expired()

Clothing: Adds size, material

Each subclass overrides __str__() to display its specific details.

2. Encapsulation
Attributes are encapsulated using protected/private access (e.g., _price, _name).

Uses @property and @setter decorators to validate and control access, such as ensuring positive prices and quantities.

3. Polymorphism
The system uses polymorphism to treat all product types uniformly. The Inventory class manages a mixed collection of products and calls shared methods (__str__, etc.) without knowing the specific subclass of each product.

4. Exception Handling
Custom exceptions are defined to handle edge cases and maintain system stability:

InsufficientStockError: Raised when trying to sell more than available stock.

DuplicateProductError: Raised when adding a product with an already used ID.

Inventory Class (Controller)
The Inventory class manages all product-related operations. It holds a dictionary of products and provides methods to:

Add or remove products

Sell and restock stock

Search products by name or type

Remove expired grocery items

Calculate total inventory value

InventoryCLI (User Interface Layer)
The main.py file provides a command-line interface for users to interact with the inventory. It displays a menu and performs actions based on user input:

Sample CLI Menu:
mathematica
Copy
Edit
1. Add Product  
2. Sell Product  
3. Restock Product  
4. Search Product by Name  
5. Search Product by Type  
6. List All Products  
7. Remove Expired Products  
8. Show Total Inventory Value  
9. Exit
Key OOP Concepts Applied
Concept	Application
Abstraction	Product abstract base class defines shared structure and behavior
Encapsulation	Properties and setters control access to internal attributes
Inheritance	Electronics, Grocery, and Clothing inherit from Product
Polymorphism	Common methods like __str__() behave differently based on product type

Conclusion
This CLI-based Inventory Management System demonstrates strong object-oriented design principles. It separates responsibilities across multiple classes, enforces data integrity with encapsulation and exception handling, and uses inheritance and polymorphism to manage diverse product types efficiently.

