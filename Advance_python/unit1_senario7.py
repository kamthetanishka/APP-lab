#7. Product Inventory System. Develop a Python application to manage product records. #Requirements
#Create a Product class with:Product ID, Product Name, Price
#Categorize products as:Expensive, Affordable
#Create an Inventory class.
#Display all products.
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = self.categorize_product()

    def categorize_product(self):
        if self.price > 1000:
            return "Expensive"
        else:
            return "Affordable"
#inventory class to manage product records
class Inventory:
    def __init__(self):
         self.products = []
    def add_product(self, product):
        self.products.append(product)
    def display_products(self):
        print("\nProduct Inventory")
        if len(self.products) == 0:
            print("Inventory is Empty")
        else:
            for product in self.products:
                print(f"Product ID: {product.product_id}, Name: {product.product_name}, Price: {product.price}, Category: {product.category}")
        print("------------------------------\n")    
        
product1 = Product(1, "Laptop", 1500)
product2 = Product(2, "Mouse", 500)
product3 = Product(3, "Keyboard", 800)
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)
inventory.display_products()
         