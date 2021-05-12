import mysql.connector as conn
import csv


# Connect to mysql-server
mydb = conn.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)
print("Hi")

# Create cusor object
cursor = mydb.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS Samaki")
print("Database created")
