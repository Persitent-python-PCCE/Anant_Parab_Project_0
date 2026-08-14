from dao.orders_dao import OrderDAO
from dao.cart_dao import CartDAO
from dao.stock_dao import StockDAO
from model.orders import Orders
from model.orderItems import OrderItems

class OrderService:
    def __init__(self):
        self.order_dao = OrderDAO()
        self.cart_dao = CartDAO()
        self.stock_dao = StockDAO()

    def place_order(self, user_id):
        cart_id = self.cart_dao.get_or_create_cart(user_id)
        items = self.cart_dao.get_cart_items(cart_id)
        
        if not items:
            raise ValueError("Cart is empty")

        total = sum(item['unit_price'] * item['quantity'] for item in items)
        
        for item in items:
            stock = self.stock_dao.get_stock_by_product(item['product_id'])
            if not stock or stock['quantity'] < item['quantity']:
                raise ValueError(f"Not enough stock for product ID {item['product_id']}")

        order = Orders(user_id=user_id, total_amount=total)
        order_id = self.order_dao.create_order(order)
        
        for item in items:
            if not self.stock_dao.reduce_stock(item['product_id'], item['quantity']):
                raise ValueError("Failed to reduce stock (concurrency issue).")
            oi = OrderItems(order_id, item['product_id'], item['quantity'], item['unit_price'])
            self.order_dao.add_order_item(oi)
            
        self.cart_dao.clear_cart(cart_id)
        return order_id

    def get_order_history(self, user_id):
        orders = self.order_dao.get_orders_by_user(user_id)
        for o in orders:
            o['items'] = self.order_dao.get_order_items(o['order_id'])
        return orders

    def get_all_orders(self):
        orders = self.order_dao.get_all_orders()
        for o in orders:
            o['items'] = self.order_dao.get_order_items(o['order_id'])
        return orders
