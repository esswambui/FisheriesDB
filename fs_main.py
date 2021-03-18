import mysql.connector as conn
import csv


# Connect to mysql-server
mydb = conn.connect(
    host="localhost",
    user="root",
    password="newlight",
    database="Fisheries"
)
print("Hi")

# Create cusor object
cursor = mydb.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS Fisheries")
print("Database created")

# Create station table
cursor.execute('''CREATE TABLE IF NOT EXISTS station (
station_id INT(3) AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
station_name VARCHAR(100) NOT NULL,
station_address VARCHAR(100))''')
print("Station table created")

# Create boat table
cursor.execute('''CREATE TABLE IF NOT EXISTS boat (
boat_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
boat_name VARCHAR(100) NOT NULL,
boat_size DECIMAL(3.2),
boat_length DECIMAL(3.2),
boat_capacity INT(2),
station_id INT(3) NOT NULL, 
fishing BOOLEAN,
  CONSTRAINT FK_boat_station
  FOREIGN KEY (station_id)
        REFERENCES station(station_id)  )''')
print("Boat table created")

# Create Owner Table
cursor.execute('''CREATE TABLE IF NOT EXISTS owner (
owner_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
owner_name VARCHAR(100) NOT NULL,
boat_id INT(5) NOT NULL UNIQUE,
phone_number INT(10) NOT NULL,
email VARCHAR(100) NOT NULL,
  CONSTRAINT FK_owner_boat
  FOREIGN KEY (boat_id)
        REFERENCES boat(boat_id)  )''')
print("Owner table created")

# Create Fishers Table
cursor.execute('''CREATE TABLE IF NOT EXISTS fisher (
fisher_id INT(5) AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
fisher_name VARCHAR(100) NOT NULL,
boat_id INT(5) NOT NULL UNIQUE,
phone_number INT(10) NOT NULL,
email VARCHAR(100) NOT NULL,
age INT(3) NOT NULL,
  CONSTRAINT FK_fisher_boat
  FOREIGN KEY (boat_id)
        REFERENCES boat(boat_id)  )''')
print("Fisher table created")

#  Insert station records from csv file
with open('D:\FisheriesDB\stations.csv', 'r') as stationrec:
    s_reader = csv.reader(stationrec)

    next(s_reader)  # dkip first ecord
    for rec in s_reader:
        cursor.execute(
            "INSERT IGNORE INTO station(station_id, station_name, station_address) VALUES(%s, %s, %s)", rec)
        mydb.commit()
print("Station records added")

#  Insert boat records from csv file
#
# Read from csv file
boatrec = csv.reader(open(r"D:\FisheriesDB\boats.csv", 'r'))
next(boatrec)  # Skip the first row

# insert records line by line
for row in boatrec:

    # cursor.execute("set foreign_key_checks=0;") -- Ignores foreugn key constaint
    cursor.execute(
        "INSERT IGNORE INTO boat(boat_id, boat_name, boat_size, boat_length, boat_capacity, station_id, fishing) VALUES(%s, %s, %s, %s, %s, %s, %s)", row)
    mydb.commit()
print("Boat records added")

#  Insert owner records from csv file
#
# Read from csv file
ownrec = csv.reader(open(r"D:\FisheriesDB\owners.csv", 'r'))
next(ownrec)  # Skip the first row
for row in ownrec:
    cursor.execute(
        "INSERT IGNORE INTO owner(owner_id, owner_name, boat_id, phone_number, email) VALUES(%s, %s, %s, %s, %s)", row)
    mydb.commit()
print("Owner records added")

#  Insert fisher records from csv file
#
# Read from csv file
fishrec = csv.reader(open(r"D:\FisheriesDB\fishers.csv", 'r'))
next(fishrec)  # Skip the first row
for row in fishrec:
    cursor.execute(
        "INSERT IGNORE INTO fisher(fisher_id, fisher_name, boat_id, phone_number, email, age) VALUES(%s, %s, %s, %s, %s, %s)", row)
    mydb.commit()
print("Fisher records added")


# function to join station and boat ewcords
def boat_station_join():
    cursor.execute(
        "SELECT * FROM boat INNER JOIN station \
         ON boat.station_id = station.station_id\
          ")
    print(" \n\t\t\t\t Boats and Stations ")
    print("______________________________________________________________________________\n")
    for j in cursor.fetchall():
        print(j)


boat_station_join()

# function to join boat owne and fishe records


def boat_owners_fishers_join():
    cursor.execute(
        "SELECT * FROM fisher INNER JOIN boat \
         ON fisher.boat_id = boat.boat_id\
          INNER JOIN owner ON owner.boat_id = boat.boat_id")

    print(" \n\t\t\t\t Fisher Records ")
    print("______________________________________________________________________________\n")
    for j in cursor.fetchall():
        print(j)


boat_owners_fishers_join()

cursor.close()
