"""
Helper file that writes the data to the csv files
"""
import csv
from station import Station

# station_id, station_name
stations = [[1, "one"], [2, "two"], [3, "three"], [4, "four"], [5, "five"], [6, "six"], [7, "seven"]]
stations_data = [Station(station[0], station[1]) for station in stations]

# user_id, user_name
users = [[1, 'foo'], [2, 'bar'], [3, 'baz']]

# ticket_id, user_id, start_station_id, destination_id, price
tickets = [[1, 2, 1, 2, 5], [2, 1, 1, 3, 5], [3, 3, 1, 2, 5], [4, 2, 1, 4, 5]]

with open("csv_files/stations.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(stations)

with open("csv_files/tickets.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(tickets)

with open("csv_files/users.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(users)