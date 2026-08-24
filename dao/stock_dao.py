from logs.logger import log_event
from config.database import get_connection

class StockDAO:
    def add_or_update_stock(self, product_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = """
                INSERT INTO stock (product_id, quantity) VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE quantity = quantity + %s
            """
            values = (product_id, quantity, quantity)
            cursor.execute(q, values)
            conn.commit()

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in add_or_update_stock: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_stock_by_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            q = "SELECT * FROM stock WHERE product_id = %s"
            cursor.execute(q, (product_id,))
            row = cursor.fetchone()
            log_event(f"DAO SUCCESS in get_stock_by_product")
            return row

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in get_stock_by_product: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def reduce_stock(self, product_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "UPDATE stock SET quantity = quantity - %s WHERE product_id = %s AND quantity >= %s"
            cursor.execute(q, (quantity, product_id, quantity))
            conn.commit()
            affected = cursor.rowcount
            log_event(f"DAO SUCCESS in reduce_stock")
            return affected > 0
        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in reduce_stock: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

