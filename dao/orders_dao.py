from config.database import get_connection

class OrderDAO:
    def create_order(self, order):
        conn = get_connection()
        cursor = conn.cursor()
        q = "INSERT INTO orders (user_id, discount, total_amount, status) VALUES (%s, %s, %s, %s)"
        values = (order.user_id, order.discount, order.total_amount, order.status)
        cursor.execute(q, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def add_order_item(self, order_item):
        conn = get_connection()
        cursor = conn.cursor()
        q = "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)"
        values = (order_item.order_id, order_item.product_id, order_item.quantity, order_item.unit_price)
        cursor.execute(q, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_orders_by_user(self, user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = "SELECT * FROM orders WHERE user_id = %s ORDER BY order_date DESC"
        cursor.execute(q, (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_order_items(self, order_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = """
            SELECT oi.product_id, p.product_name, oi.quantity, oi.unit_price 
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = %s
        """
        cursor.execute(q, (order_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_all_orders(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = "SELECT * FROM orders ORDER BY order_date DESC"
        cursor.execute(q)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
