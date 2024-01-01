import mysql.connector as mysql
import db_config
from mysql_class import MySQL


class MySQL_DB:
    def __init__(self):
        self.MySQL = MySQL()
        self.conn = None
        self.cursor = None
        self.connect() # koneksi ke lokal db

    def connect(self):
        self.conn = mysql.connect(**db_config.dbConfig)
        self.cursor = self.conn.cursor()

    def create_db(self, db_name):
        try:
            self.cursor.execute("CREATE DATABASE {} \
                    DEFAULT CHARACTER SET 'utf8'".format(db_name))
            return db_name
        except mysql.Error as err:
            print("Failed to create DB: {}".format(err))
