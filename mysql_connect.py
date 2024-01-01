import mysql.connector as mysql
import db_config

# user="root", password="", host="127.0.0.1"
# conn = mysql.connect(user="root", password="1234", host="127.0.0.1", port=3316)
conn = mysql.connect(**db_config.dbConfig)
print(conn)

# conn.close()

cursor = conn.cursor()

# def connect_db():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="1234",
#         database="mahasiswa",
#         port=3316
#     )
