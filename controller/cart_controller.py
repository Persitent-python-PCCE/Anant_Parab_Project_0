from service.cart_service import CartService
from service.product_service import ProductService

class CartController:
    def __init__(self):
        self.cart_service = CartService()
        self.product_service = ProductService()

    def add_to_cart(self, user_id):
        print("\n--- Add to Cart ---")
        products = self.product_service.get_all_products()
        for p in products:
            print(f"ID: {p['product_id']} | Name: {p['product_name']} | Price: {p['unit_price']}")
        
        p_id = int(input("Enter product ID to add: "))
        quantity = int(input("Enter quantity: "))
        
        self.cart_service.add_to_cart(user_id, p_id, quantity)
        print("Item added to cart.")

    def view_cart(self, user_id):
        print("\n--- View Cart ---")
        items = self.cart_service.view_cart(user_id)
        if not items:
            print("Cart is empty.")
            return

        total = 0
        for i in items:
            cost = i['unit_price'] * i['quantity']
            total += cost
            print(f"Product: {i['product_name']} | Qty: {i['quantity']} | Unit Price: {i['unit_price']} | Subtotal: {cost}")
        print(f"Total: {total}")

    def remove_from_cart(self, user_id):
        print("\n--- Remove from Cart ---")
        p_id = int(input("Enter product ID to remove: "))
        affected = self.cart_service.remove_from_cart(user_id, p_id)
        if affected:
            print("Item removed from cart.")
        else:
            print("Item not found in cart.")
