import mysql.connector as mysql
import db_config

GUIDB = "GuiDB"

# unpack dictionary credentials
conn = mysql.connect(db_config)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

conn.close()
