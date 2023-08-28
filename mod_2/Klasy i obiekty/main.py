from shop.apple import Apple
from shop.potato import Potato
from shop.product import Product
from shop.order import Order, generate_random_order

if __name__ == "__main__":
    apple_jonagold = Apple("Jonagold", "L", 3.50)
    apple_champion = Apple("Champion", "XL", 3.99)

    print(f"Jonagold name: {apple_jonagold.grade_name}")
    print(f"Jonagold size: {apple_jonagold.size}")
    print(f"Jonagold price: {apple_jonagold.price}")
    print(f"Champion name: {apple_champion.grade_name}")
    print(f"Champion size: {apple_champion.size}")
    print(f"Champion price: {apple_champion.price}")

    jonagold_total_price = apple_jonagold.total_price(kilograms=5)
    champion_total_price = apple_champion.total_price(kilograms=7)

    print(f"Jonagold total price: {jonagold_total_price}")
    print(f"Champion total price: {champion_total_price}")

    my_potato = Potato(grade_name="Bryza", size="M", price=2.99)

    print(f"my_potato name: {my_potato.grade_name}")
    print(f"my_potato size: {my_potato.size}")
    print(f"my_potato price: {my_potato.price}")

    bryza_total_price = my_potato.total_price(5)

    print(f"Bryza total price: {bryza_total_price:.2f}")

    products = [
        Product("Milk", "dairy", 3.50),
        Product("Bread", "breadstuff", 4.50),
        Product("Coca-Cola", "beverages", 7.99)
    ]

    for product in products:
        product.print_product_details()

    orders = []

    order_1 = Order("Kamil", "Kowalski", products)
    order_2 = Order("Maja", "Walczak", products)

    orders.append(order_1)
    orders.append(order_2)

    for order in orders:
        order.print_order_details()

    random_order = generate_random_order("Jan", "Kowalski")

    random_order.print_order_details()
