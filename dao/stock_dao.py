from config.database import get_connection

class StockDAO:
    def add_or_update_stock(self, product_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        q = """
            INSERT INTO stock (product_id, quantity) VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE quantity = quantity + %s
        """
        values = (product_id, quantity, quantity)
        cursor.execute(q, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_stock_by_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = "SELECT * FROM stock WHERE product_id = %s"
        cursor.execute(q, (product_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def reduce_stock(self, product_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        q = "UPDATE stock SET quantity = quantity - %s WHERE product_id = %s AND quantity >= %s"
        cursor.execute(q, (quantity, product_id, quantity))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected > 0
