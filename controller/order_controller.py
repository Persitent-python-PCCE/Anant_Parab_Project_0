from logs.logger import log_event
from service.order_service import OrderService

class OrderController:
    def __init__(self):
        self.order_service = OrderService()

    def place_order(self, user_id):
        try:
            print("\n--- Place Order ---")
            o_id = self.order_service.place_order(user_id)
            print("Order placed successfully! Order ID:", o_id)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in place_order: {e}")

    def view_order_history(self, user_id):
        try:
            print("\n--- Order History ---")
            orders = self.order_service.get_order_history(user_id)
            if not orders:
                print("No orders found.")
                return
            
            for o in orders:
                print(f"Order ID: {o['order_id']} | Date: {o['order_date']} | Total: {o['total_amount']} | Status: {o['status']}")
                for item in o['items']:
                    print(f"   -> {item['product_name']} | Qty: {item['quantity']} | Price: {item['unit_price']}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in view_order_history: {e}")

    def view_all_orders(self):
        try:
            print("\n--- All Orders (Admin) ---")
            orders = self.order_service.get_all_orders()
            for o in orders:
                print(f"Order ID: {o['order_id']} | User ID: {o['user_id']} | Total: {o['total_amount']} | Status: {o['status']}")
                for item in o['items']:
                    print(f"   -> {item['product_name']} | Qty: {item['quantity']} | Price: {item['unit_price']}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in view_all_orders: {e}")

