import random

from shop.product import Product


class Order:
    def __init__(self, first_name, last_name, products=None):
        self.first_name = first_name
        self.last_name = last_name

        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.price
        self.total_price = total_price

    def print_order_details(self):
        print(f"Customer first name: {self.first_name}\nCustomer last name: {self.last_name}\nTotal price:  {self.total_price}")
        print("Products:\n")
        for product in self.products:
            product.print_product_details()


def generate_random_order(first_name, last_name):
    number_of_products = random.randint(1, 20)
    random_products = []

    for product_number in range(number_of_products):
        product_name = "Product_" + str(product_number)
        category = "Category_" + str(product_number)
        price = product_number

        random_products.append(Product(product_name, category, price))

    random_order = Order(first_name, last_name, random_products)

    return random_order



