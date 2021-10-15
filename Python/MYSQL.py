#             MYSQL

# pip install mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="name",
  password="password"
)

query = "DROP DATABASE ...";

cursor = db.cursor()
result = cursor.execute(query)