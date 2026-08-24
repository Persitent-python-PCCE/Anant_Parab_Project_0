import mysql.connector

def get_connection():
  connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "X3raV5VrcMzt4x4U3nj5",
    database = "ecommerce"
  )
  return connection