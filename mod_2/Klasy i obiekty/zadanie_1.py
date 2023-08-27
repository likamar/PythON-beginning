class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == "__main__":
    apple_1 = Apple()
    apple_2 = Apple()
    apple_3 = Apple()
    potato_1 = Potato()
    potato_2 = Potato()

    print(f"First apple class: {type(apple_1)}")
    print(f"Second apple class: {type(apple_2)}")
    print(f"Third apple class: {type(apple_3)}")
    print(f"First potato class: {type(potato_1)}")
    print(f"Second potato class: {type(potato_2)}")

    orders = []

    for order in range(5):
        orders.append(Order())

    print(orders)

    products = {
        "milk": Product(),
        "bread": Product(),
        "coca-cola": Product()
    }

    print(products)