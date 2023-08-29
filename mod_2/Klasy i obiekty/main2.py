from shop.order import generate_random_order


def run_homework():
    first_order = generate_random_order(first_name="Michał", last_name="Jagielski")
    first_order.print_order_details()
    second_order = generate_random_order(first_name="Joanna", last_name="Kluska")
    second_order.print_order_details()


if __name__ == "__main__":
    run_homework()