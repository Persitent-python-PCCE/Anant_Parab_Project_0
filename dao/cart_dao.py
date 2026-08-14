from config.database import get_connection

class CartDAO:
    def get_or_create_cart(self, user_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
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
            
        cursor.close()
        conn.close()
        return cart_id

    def add_item_to_cart(self, cart_item):
        conn = get_connection()
        cursor = conn.cursor()
        q = "INSERT INTO cart_items (cart_id, product_id, quantity) VALUES (%s, %s, %s)"
        values = (cart_item.cart_id, cart_item.product_id, cart_item.quantity)
        cursor.execute(q, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_cart_items(self, cart_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = """
            SELECT ci.product_id, p.product_name, p.unit_price, ci.quantity 
            FROM cart_items ci
            JOIN products p ON ci.product_id = p.product_id
            WHERE ci.cart_id = %s
        """
        cursor.execute(q, (cart_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def remove_item_from_cart(self, cart_id, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        q = "DELETE FROM cart_items WHERE cart_id = %s AND product_id = %s"
        cursor.execute(q, (cart_id, product_id))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected

    def clear_cart(self, cart_id):
        conn = get_connection()
        cursor = conn.cursor()
        q = "DELETE FROM cart_items WHERE cart_id = %s"
        cursor.execute(q, (cart_id,))
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected
