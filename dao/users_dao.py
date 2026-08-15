from config.database import get_connection

class UserDAO:
  def add_user(self, user):
    conn = get_connection()
    cursor = conn.cursor()
    q = "INSERT INTO users (user_name, age, contact_number, email, password, role) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (user.user_name, user.age, user.contact_number, user.email, user.password, user.role)
    cursor.execute(q, values)
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return user_id

  def log_in(self, email, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    q = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(q, values)
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

  def get_all_users(self, ):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # q = "SELECT * FROM users WHERE role = %s"
    q = "SELECT * FROM users"
    cursor.execute(q)
    user = cursor.fetchall()
    cursor.close()
    conn.close()
    return user
