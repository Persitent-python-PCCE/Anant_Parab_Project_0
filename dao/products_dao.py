from logs.logger import log_event
from config.database import get_connection

class ProductDAO:
    def add_product(self, product):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "INSERT INTO products (product_name, category_id, unit_price) VALUES (%s, %s, %s)"
            values = (product.product_name, product.category_id, product.unit_price)
            cursor.execute(q, values)
            conn.commit()
            new_id = cursor.lastrowid
            log_event(f"DAO SUCCESS in add_product")
            return new_id

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in add_product: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_all_products(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            q = "SELECT * FROM products"
            cursor.execute(q)
            rows = cursor.fetchall()
            log_event(f"DAO SUCCESS in get_all_products")
            return rows

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in get_all_products: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_product_by_id(self, product_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            q = "SELECT * FROM products WHERE product_id = %s"
            values = (product_id,)
            cursor.execute(q, values)
            row = cursor.fetchone()
            log_event(f"DAO SUCCESS in get_product_by_id")
            return row

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in get_product_by_id: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def update_product(self, product):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "UPDATE products SET product_name = %s, category_id = %s, unit_price = %s WHERE product_id = %s"
            values = (product.product_name, product.category_id, product.unit_price, product.product_id)
            cursor.execute(q, values)
            conn.commit()
            affected = cursor.rowcount
            log_event(f"DAO SUCCESS in update_product")
            return affected

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in update_product: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def delete_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "DELETE FROM products WHERE product_id = %s"
            values = (product_id,)
            cursor.execute(q, values)
            conn.commit()
            affected = cursor.rowcount
            log_event(f"DAO SUCCESS in delete_product")
            return affected
        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in delete_product: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

