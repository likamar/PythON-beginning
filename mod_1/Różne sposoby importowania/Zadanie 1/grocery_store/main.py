from shopping.order import create_new_order, orders


def run_shop():
    print("Welcome to Grocery Store!")

    product_name = input("Product name: ")
    quantity = int(input("How much: "))
    customer_order = create_new_order(product_name, quantity)

    if customer_order is not None:
        print(f"Your order: {customer_order}")


if __name__ == "__main__":
    run_shop()