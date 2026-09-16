import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

class DataBase:
    def __init__(self):
        self.db_server = os.getenv("DB_SERVER")
        self.db_port = int(os.getenv("DB_PORT"))
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_database = os.getenv("DB_DATABASE")
        
        
    def conexion(self):
        con1 = pymysql.connect(host=self.db_server,user=self.db_user,port=self.db_port,password=self.db_password,database=self.db_database,cursorclass=pymysql.cursors.DictCursor)
        return con1;
    
    def get_categories(self):
        con1 = self.conexion()
        result=""
        with con1:
            with con1.cursor() as cursor:
                sql="SELECT * from tb_categories ORDER BY orden ASC"
                cursor.execute(sql)
                result = cursor.fetchall()
        return result