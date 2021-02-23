import mysql.connector

class database():
    def __init__(self, instance, username, password):
        self.db = mysql.connector.connect(host=instance, user=username, password=password, database="lottodb")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM draws")

        table_list = self.cursor.fetchall()
        for x in table_list:
            print(x)
            