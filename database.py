import mysql.connector

class database():
    def __init__(self, instance, username, password):
        self.db = mysql.connector.connect(host=instance, user=username, password=password, database="lotto")
        self.cursor = self.db.cursor()
        self.cursor.execute("SHOW TABLES")
        for x in self.cursor:
            print(x)
