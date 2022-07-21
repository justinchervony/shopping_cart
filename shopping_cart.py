import product
class ShoppingCart:
    def __init__(self):
        self.products_in_cart = []
    
    def price_of_products_in_cart(self):
        total_price = 0
        for item in self.products_in_cart:
            total_price += item.price
        return total_price

    def add_new_product(self, product_to_add):
        self.products_in_cart.append(product_to_add)