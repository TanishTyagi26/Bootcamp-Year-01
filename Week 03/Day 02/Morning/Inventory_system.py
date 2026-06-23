# Task: Simulating a simple inventory system with object lists

# Use a constructor and a loop to create and manage multiple Product objects

# Create a class Product with _init_(self, name, price, quantity) and a method total_value() returning price quantity. Using a list of (name, price, quantity) tuples, create a Product object for each one in a loop, store them in a list, then loop through and print each product's total value plus the grand total inventory value.



class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_value(self):
        return self.price*self.quantity

products_data = [("KeyChains", 500, 2),("Rings", 50, 10),("colours", 150, 5)]
products=[]

for name, price, quantity in products_data:
    p = Product(name, price, quantity)
    products.append(p)

grand_total = 0

for product in products:
    value = product.total_value()
    grand_total += value

    print(f"Product: {product.name}")
    print(f"Total Value: ${value}")
    print()

print(f"Grand Total Inventory Value: ${grand_total}")