# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="codebind",
    password="pwd123",
)

# prepare a cursor object using cursor() method
cursor_obj = database.cursor()

# create a database
cursor_obj.execute("CREATE DATABASE dbweb;")
print("Database created successfully")
