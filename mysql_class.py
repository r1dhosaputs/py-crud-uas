import MySQLdb as mysql
import db_config

# bersihkan setelah digunakan koneksinya
# def close(self, cursor, conn):
#     # close cursor
#     cursor.close()


#     # close connection to MySQL
#     conn.close()
class MySQL:
    DB = "mahasiswa"

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.currentdb = None

    # koneksi ke database
    def connect(self):
        self.conn = mysql.connect(**db_config.dbConfig)
        self.cursor = self.conn.cursor()

    # tutup koneksi
    def close(self, cursor, conn):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    def useDB(self, db_name):
        self.connect()
        try:
            self.cursor.execute("USE {}".format(db_name))
            self.currentdb = db_name
            return "Switched to database {}.".format(db_name)
        except mysql.Error as err:
            return "Failed to switch database: {}".format(err)

    def showData(self, tb_name):
        self.connect()
        self.useDB("mahasiswa")
        try:
            self.cursor.execute("SELECT * FROM {}".format(tb_name))
            result = self.cursor.fetchall()
            return result
        except mysql.Error as err:
            return "Failed to show data: {}".format(err)

    def insertData(self, data):
        self.connect()
        self.useDB("mahasiswa")
        
        if not data:
            return False

        try:
            self.cursor.execute(
                "INSERT INTO mahasiswa (nama,nim,jenis_kelamin) VALUES (%s, %s, %s)",
                (data["name"], data["nim"], data["gender"]),
            )
            self.conn.commit()
            self.cursor.close()

            return True

        except mysql.Error as err:
            return "Fail: {}".format(err)

    def deleteData(self, id):
        self.connect()
        try:
            self.useDB("mahasiswa")
            self.cursor.execute("DELETE FROM mahasiswa WHERE id=%s", (id,))
            self.conn.commit()
            self.conn.close()
            return True
        except mysql.Error as err:
            return "Fail: {}".format(err)

    def editData(self, data):
        self.connect()
        # data = {"name": "refa", "nim": "31313131", "gender": "Perempuan", "id": 42}
        try:
            self.useDB("mahasiswa")
            self.cursor.execute(
                "UPDATE mahasiswa SET nama=%s, nim=%s, jenis_kelamin=%s WHERE id=%s",
                (data["name"], data["nim"], data["gender"], int(data["id"])),
            )
            self.conn.commit()
            self.conn.close()
            return True
        except mysql.Error as err:
            return "Fail :{}".format(err)


if __name__ == "__main__":
    # Create class instance
    mySQL = MySQL()

# test = MySQL()
# test.showDB()
# db = test.useDB("mahasiswa")
# test.insertData()
# print(test.showData("mahasiswa"))
# print(test.connect())

# def showTables(self):
#     self.connect()
#     self.useDB(self.currentdb)
#     try:
#         self.cursor.execute("SHOW TABLES")
#         tables = self.cursor.fetchall()
#         print("Tables in the current database:")
#         for table in tables:
#             print(table[0])
#     except mysql.Error as err:
#         print("Failed to show tables: {}".format(err))
#     finally:
#         pass
