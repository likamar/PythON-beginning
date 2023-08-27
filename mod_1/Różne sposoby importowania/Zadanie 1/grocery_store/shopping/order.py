from shopping.products import products, update_product_quantity


orders = []


def create_new_order(product_name, quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]

    if quantity > available_quantity:
        print(f"We don't have so much {product_name}. Only {available_quantity} left.")
        return None

    total_price = price * quantity
    new_order = {
        "product": product_name,
        "quantity": quantity,
        "total_price": total_price
    }

    update_product_quantity(product_name, quantity)
    orders.append(new_order)
    return new_order
