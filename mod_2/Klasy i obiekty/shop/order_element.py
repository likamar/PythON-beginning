class OrderElement():
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def print_order_element(self):
        self.product.print_product_details()
        print(f"quantity: {self.quantity}\n")


