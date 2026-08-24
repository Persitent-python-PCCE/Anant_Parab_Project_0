from logs.logger import log_event
from config.database import get_connection

class CartDAO:
    def get_or_create_cart(self, user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            q = "SELECT cart_id FROM cart WHERE user_id = %s"
            cursor.execute(q, (user_id,))
            row = cursor.fetchone()
        
            if row:
                cart_id = row['cart_id']
            else:
                q2 = "INSERT INTO cart (user_id) VALUES (%s)"
                cursor.execute(q2, (user_id,))
                conn.commit()
                cart_id = cursor.lastrowid
            
            log_event(f"DAO SUCCESS in get_or_create_cart")
            return cart_id

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in get_or_create_cart: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def add_item_to_cart(self, cart_item):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "INSERT INTO cart_items (cart_id, product_id, quantity) VALUES (%s, %s, %s)"
            values = (cart_item.cart_id, cart_item.product_id, cart_item.quantity)
            cursor.execute(q, values)
            conn.commit()
            new_id = cursor.lastrowid
            log_event(f"DAO SUCCESS in add_item_to_cart")
            return new_id

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in add_item_to_cart: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_cart_items(self, cart_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            q = """
                SELECT ci.product_id, p.product_name, p.unit_price, ci.quantity 
                FROM cart_items ci
                JOIN products p ON ci.product_id = p.product_id
                WHERE ci.cart_id = %s
            """
            cursor.execute(q, (cart_id,))
            rows = cursor.fetchall()
            log_event(f"DAO SUCCESS in get_cart_items")
            return rows

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in get_cart_items: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def remove_item_from_cart(self, cart_id, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "DELETE FROM cart_items WHERE cart_id = %s AND product_id = %s"
            cursor.execute(q, (cart_id, product_id))
            conn.commit()
            affected = cursor.rowcount
            log_event(f"DAO SUCCESS in remove_item_from_cart")
            return affected

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in remove_item_from_cart: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def clear_cart(self, cart_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "DELETE FROM cart_items WHERE cart_id = %s"
            cursor.execute(q, (cart_id,))
            conn.commit()
            affected = cursor.rowcount
            log_event(f"DAO SUCCESS in clear_cart")
            return affected
        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in clear_cart: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

