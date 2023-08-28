class Potato:
    def __init__(self, grade_name, size, price):
        self.grade_name = grade_name
        self.size = size
        self.price = price

    def total_price(self, quantity_kilograms):
        return self.price * quantity_kilograms
