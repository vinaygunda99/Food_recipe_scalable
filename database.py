
""" 
import mysql.connector
from mysql.connector import errorcode
def create_connection():

    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',  
        'database': 'recipe_generator',
        'raise_on_warnings': True
    }
    try:
        conn = mysql.connector.connect(**config)
        print("Connection successful.")
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(f"Error: {err}")
        return None
 """



import pymysql

def create_connection():
    
    config = {
        'user': 'admin',
        'password': 'x23302712-recipe-rds',
        'host': 'x23302712-recipe-rds.cewtwnkkj49j.eu-central-1.rds.amazonaws.com',  
        'database': 'x23302712-recipe-rds'
    }
    try:
        conn = pymysql.connect(**config)
        print("Connection successful.")
        return conn
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None