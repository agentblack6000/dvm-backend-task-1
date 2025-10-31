"""
Helper file that reads data from csv files and provides it where necessary
"""
import csv

from user import User
from station import Station

# station_id, station_name
stations = []
stations_data = []

# user_id, user_name
users = []

tickets = []

with open("csv_files/stations.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        stations.append([int(row[0]), row[1]])

stations_data = [Station(station[0], station[1]) for station in stations]

with open("csv_files/users.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        users.append([int(row[0]), row[1]])

with open("csv_files/tickets.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        tickets.append(row)

user_names = []
users = []

with open("csv_files/users.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    for user_data in reader:
        user_names.append(user_data[1])
        users.append(User(id=int(user_data[0]), name=user_data[1]))