# main.py

from inventory import Inventory
from product import Electronics, Grocery, Clothing
from product import DuplicateProductError, InsufficientStockError, InvalidProductDataError


class InventoryCLI:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        print("Inventory Management System")
        print("--------------------------")

        while True:
            print("\nMenu:")
            print("1. Add Product")
            print("2. Sell Product")
            print("3. Search/View Products")
            print("4. Save Inventory")
            print("5. Load Inventory")
            print("6. Remove Expired Groceries")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            try:
                if choice == '1':
                    self._add_product_menu()
                elif choice == '2':
                    self._sell_product_menu()
                elif choice == '3':
                    self._search_view_menu()
                elif choice == '4':
                    self._save_inventory_menu()
                elif choice == '5':
                    self._load_inventory_menu()
                elif choice == '6':
                    expired = self.inventory.remove_expired_products()
                    print(f"Removed {len(expired)} expired grocery items")
                elif choice == '7':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def _add_product_menu(self):
        print("\nAdd Product:")
        print("1. Electronics")
        print("2. Grocery")
        print("3. Clothing")
        print("4. Back to Main Menu")

        choice = input("Enter product type (1-4): ")
        if choice == '4':
            return

        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter initial stock quantity: "))

        if choice == '1':
            warranty = int(input("Enter warranty years: "))
            brand = input("Enter brand: ")
            product = Electronics(product_id, name, price, quantity, warranty, brand)
        elif choice == '2':
            expiry = input("Enter expiry date (YYYY-MM-DD): ")
            product = Grocery(product_id, name, price, quantity, expiry)
        elif choice == '3':
            size = input("Enter size: ")
            material = input("Enter material: ")
            product = Clothing(product_id, name, price, quantity, size, material)
        else:
            print("Invalid choice")
            return

        self.inventory.add_product(product)
        print("Product added successfully!")

    def _sell_product_menu(self):
        product_id = input("Enter product ID to sell: ")
        quantity = int(input("Enter quantity to sell: "))

        self.inventory.sell_product(product_id, quantity)
        print("Sale completed successfully!")

    def _search_view_menu(self):
        print("\nSearch/View Options:")
        print("1. Search by Name")
        print("2. View All Products")
        print("3. View Electronics")
        print("4. View Groceries")
        print("5. View Clothing")
        print("6. View Inventory Value")
        print("7. Back to Main Menu")

        choice = input("Enter your choice (1-7): ")
        if choice == '7':
            return

        if choice == '1':
            name = input("Enter name to search: ")
            products = self.inventory.search_by_name(name)
        elif choice == '2':
            products = self.inventory.list_all_products()
        elif choice == '3':
            products = self.inventory.search_by_type(Electronics)
        elif choice == '4':
            products = self.inventory.search_by_type(Grocery)
        elif choice == '5':
            products = self.inventory.search_by_type(Clothing)
        elif choice == '6':
            value = self.inventory.total_inventory_value()
            print(f"\nTotal Inventory Value: ${value:.2f}")
            return
        else:
            print("Invalid choice")
            return

        if not products:
            print("No products found")
        else:
            print("\nProducts:")
            for product in products:
                print(f"- {product}")

    def _save_inventory_menu(self):
        filename = input("Enter filename to save inventory: ")
        self.inventory.save_to_file(filename)
        print("Inventory saved successfully!")

    def _load_inventory_menu(self):
        filename = input("Enter filename to load inventory: ")
        self.inventory.load_from_file(filename)
        print("Inventory loaded successfully!")


# Entry point
if __name__ == "__main__":
    cli = InventoryCLI()
    cli.run()
