"""
Helper file that writes the data to the csv files
"""
import csv
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