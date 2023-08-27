products = {
    "bread": {
        "quantity": 100,
        "price": 4
    },
    "butter": {
        "quantity": 50,
        "price": 5.99,
    },
    "tomatos": {
        "quantity": 100,
        "price": 12.99
    }
}


def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity