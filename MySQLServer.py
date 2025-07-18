import mysql.connector
from mysql.connector import Error

# Replace with your connection details
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="uche",
        password="skywalker291",
        database="alx_book_store"
)

    if mydb.is_connected():

        print(mydb.get_server_info())
        print("connected to MySQL Server...")

        mycursor = mydb.cursor()
        db_name = "alx_book_store"

        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

        if mycursor.statement.startswith("CREATE DATABASE") and mycursor.rowcount == -1:
            print(f"Database '{db_name}' already exists.")
    
        else:    
            print(f"Database '{db_name}' created successfully.")

        mycursor.close()
        mydb.close()
    
except Error as err:
    print(f"Error connecting to Mysql: {err}")

