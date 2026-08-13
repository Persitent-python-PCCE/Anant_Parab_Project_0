from config.database import get_connection;
class UserDAO:
  def add_user(self, user):
    connection = get_connection()
    cursor = connection.cursor()
    # try:
    # except:
    # else:
    q = "INSERT INTO users (user_name, age, contact_number, email, password, role) VALUE (%s,%s,%s,%s,%s,%s)"
    values = (user.user_name, user.age, user.contact_number, user.email, user.password, user.role)
    cursor.execute(q, values)
    connection.commit()

    user_id = cursor.lastrowid
    cursor.close()
    connection.close()

    return user_id

  def log_in(self, email, password):
    connection = get_connection()
    cursor = connection.cursor()
    q = "SELECT * FROM users WHERE email = %s AND password = %s "
    values = (email, password)
    cursor.execute(q, values)
    
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user

