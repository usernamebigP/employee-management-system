from mysql.connector import MySQLConnection,Error


class Database():
    def __init__(self,user,password):
        self.user=user
        self.password=password

    def callDatabase(self):
        try:
            db=MySQLConnection(host="localhost",user=self.user,password=self.password,database="airindia")
            return db

        except Error as e:
            return e
       
