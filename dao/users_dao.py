from config.database import get_connection

class UserDAO:
  def add_user(self, user):
    connection = get_connection()
    cursor = connection.cursor()
    q = "INSERT INTO users (user_name, age, contact_number, email, password, role) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (user.user_name, user.age, user.contact_number, user.email, user.password, user.role)
    cursor.execute(q, values)
    connection.commit()
    user_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return user_id

  def log_in(self, email, password):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    q = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    cursor.execute(q, values)
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

  def get_user_by_id(self, user_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    q = "SELECT * FROM users WHERE user_id = %s"
    values = (user_id,)
    cursor.execute(q, values)
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user
