class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def print_product_details(self):
        print(f"Product name: {self.name}\nProduct category: {self.category}\nProduct price: {self.price}\n")



