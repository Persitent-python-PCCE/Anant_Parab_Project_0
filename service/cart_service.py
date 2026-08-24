from logs.logger import log_event
from dao.cart_dao import CartDAO
from dao.stock_dao import StockDAO
from model.cartItmes import CartItems

class CartService:
    def __init__(self):
        self.cart_dao = CartDAO()
        self.stock_dao = StockDAO()

    def add_to_cart(self, user_id, product_id, quantity):
        if quantity <= 0:
            log_event("Validation failed: " + str("Quantity must be greater than 0"))
            raise ValueError("Quantity must be greater than 0")
            
        stock = self.stock_dao.get_stock_by_product(product_id)
        if not stock or stock['quantity'] < quantity:
            log_event("Validation failed: " + str("Not enough stock available"))
            raise ValueError("Not enough stock available")

        cart_id = self.cart_dao.get_or_create_cart(user_id)
        cart_item = CartItems(cart_id, product_id, quantity)
        log_event("Service operation successful")
        return self.cart_dao.add_item_to_cart(cart_item)

    def view_cart(self, user_id):
        cart_id = self.cart_dao.get_or_create_cart(user_id)
        log_event("Service operation successful")
        return self.cart_dao.get_cart_items(cart_id)

    def remove_from_cart(self, user_id, product_id):
        cart_id = self.cart_dao.get_or_create_cart(user_id)
        log_event("Service operation successful")
        return self.cart_dao.remove_item_from_cart(cart_id, product_id)

    def clear_cart(self, user_id):
        cart_id = self.cart_dao.get_or_create_cart(user_id)
        log_event("Service operation successful")
        return self.cart_dao.clear_cart(cart_id)
