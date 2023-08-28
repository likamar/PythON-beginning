class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


def print_product_details(product):
    print(product.name, product.category, product.price, sep=",")
