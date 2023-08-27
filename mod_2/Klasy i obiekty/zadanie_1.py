class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order:
    def __init__(self, first_name, last_name, products=None):
        self.first_name = first_name
        self.last_name = last_name
        self.products = products
        self.total_price = 0
        for product in products:
            self.total_price += product.price


class Apple:
    def __init__(self, grade_name, size, price):
        self.grade_name = grade_name
        self.size = size
        self.price = price


class Potato:
    def __init__(self, grade_name, size, price):
        self.grade_name = grade_name
        self.size = size
        self.price = price


if __name__ == "__main__":
    apple_jonagold = Apple("Jonagold", "L", 3.50)
    apple_champion = Apple("Champion", "XL", 3.99)

    print(f"Jonagold name: {apple_jonagold.grade_name}")
    print(f"Jonagold size: {apple_jonagold.size}")
    print(f"Jonagold price: {apple_jonagold.price}")
    print(f"Champion name: {apple_champion.grade_name}")
    print(f"Champion size: {apple_champion.size}")
    print(f"Champion price: {apple_champion.price}")

    products = [
        Product("Milk", "dairy", 3.50),
        Product("Bread", "breadstuff", 4.50),
        Product("Coca-Cola", "beverages", 7.99)
    ]

    orders = []

    order_1 = Order("Kamil", "Kowalski", products)
    order_2 = Order("Maja", "Walczak", products)

    orders.append(order_1)
    orders.append(order_2)

    def print_product_details(product):
        print(product.name, product.category, product.price, sep=",")

    def print_order_details(order):
        print(order.first_name, order.last_name, order.total_price, sep=",")
        for product in order.products:
            print_product_details(product)

    for order in orders:
        print_order_details(order)