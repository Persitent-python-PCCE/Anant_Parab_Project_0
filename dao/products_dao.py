from config.database import get_connection

class ProductDAO:
    def add_product(self, product):
        conn = get_connection()
        cursor = conn.cursor()
        q = "INSERT INTO products (product_name, category_id, unit_price) VALUES (%s, %s, %s)"
        values = (product.product_name, product.category_id, product.unit_price)
        cursor.execute(q, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_all_products(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = "SELECT * FROM products"
        cursor.execute(q)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_product_by_id(self, product_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = "SELECT * FROM products WHERE product_id = %s"
        values = (product_id,)
        cursor.execute(q, values)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row

    def update_product(self, product):
        conn = get_connection()
        cursor = conn.cursor()
        q = "UPDATE products SET product_name = %s, category_id = %s, unit_price = %s WHERE product_id = %s"
        values = (product.product_name, product.category_id, product.unit_price, product.product_id)
        cursor.execute(q, values)
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected

    def delete_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        q = "DELETE FROM products WHERE product_id = %s"
        values = (product_id,)
        cursor.execute(q, values)
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected
