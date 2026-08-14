from config.database import get_connection

class CategoryDAO:
    def add_category(self, category):
        conn = get_connection()
        cursor = conn.cursor()
        q = "INSERT INTO categories (category_name) VALUES (%s)"
        values = (category.category_name,)
        cursor.execute(q, values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_all_categories(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        q = "SELECT * FROM categories"
        cursor.execute(q)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
