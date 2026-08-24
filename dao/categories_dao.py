from logs.logger import log_event
from config.database import get_connection

class CategoryDAO:
    def add_category(self, category):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            q = "INSERT INTO categories (category_name) VALUES (%s)"
            values = (category.category_name,)
            cursor.execute(q, values)
            conn.commit()
            new_id = cursor.lastrowid
            log_event(f"DAO SUCCESS in add_category")
            return new_id

        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in add_category: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

    def get_all_categories(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            q = "SELECT * FROM categories"
            cursor.execute(q)
            rows = cursor.fetchall()
            log_event(f"DAO SUCCESS in get_all_categories")
            return rows
        except Exception as e:
            if 'conn' in locals(): conn.rollback()
            log_event(f"DAO ERROR in get_all_categories: {e}")
            raise e
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()

