import random

from shop.product import Product
from shop.order_element import OrderElement


class Order:
    def __init__(self, first_name, last_name, order_elements=None):
        self.first_name = first_name
        self.last_name = last_name

        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for order_element in self.order_elements:
            total_price += order_element.calculate_total_price()
        return total_price

    def print_order_details(self):
        print("/" * 30)
        print(f"Customer first name: {self.first_name}\nCustomer last name: {self.last_name}\nTotal price:  {self.total_price}")
        print("Order Elements:\n")
        for order_element in self.order_elements:
            order_element.print_order_element()


def generate_random_order(first_name, last_name):
    number_of_products = random.randint(1, 5)
    random_order_elements = []

    for product_number in range(number_of_products):
        product_name = "Product_" + str(product_number)
        category = "Category_" + str(product_number)
        price = product_number
        random_product = Product(name=product_name, category=category, price=price)
        quantity = product_number

        random_order_elements.append(OrderElement(random_product, quantity))

    random_order = Order(first_name, last_name, random_order_elements)

    return random_order



