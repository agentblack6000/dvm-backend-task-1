"""
DVM Backend Task 1
Your task is to write a command-line app that allows users to purchase tickets to travel from one 
metro station to another. You’re required to use the concepts of Object Oriented Programming to 
achieve this.

Using argument parser, gets the command-line arguments and updates the database in case of a 
new ticket purchase.
"""
import csv
import uuid

from argparse import ArgumentParser
from creator import stations_data, tickets, users, user_names
from railway_network import undergound_network
from ticket import Ticket
from map import map_maker

# Configure ArgumentParser
parser = ArgumentParser(prog="Metro Ticket Purchasing System", 
                                 description="A metro ticket purchasing system")

parser.add_argument("--user", required=True, choices=user_names)
parser.add_argument("-s", "--station", action='store_true', help="Shows a list of all available stations")
parser.add_argument("-p", "--purchase", nargs=2, choices=[station.name for station in stations_data],
                    help="Purchase a ticket from station to station", metavar=('station_A', 'station_B'))
parser.add_argument("-v", "--view", action='store_true', help="View all purchased tickets.")
parser.add_argument("-m", "--map", action='store_true', help="Display the map")

# Get the command-line arguments the user provided
args = parser.parse_args()
show_stations = args.station
show_tickets = args.view
show_map = args.map
route = args.purchase

user_name = args.user

# Get user id from the database
user_id = None
for user in users:
    if user_name == user[1]:
        user_id = int(user[0])

if show_stations:
    print("The list of stations available are:")
    for station in stations_data:
        print(station.name)

if show_tickets:
    station_ids = {station.id: station for station in stations_data}
    for ticket in tickets:
        if int(ticket[1]) == user_id:
            print(f"{user_name} has a ticket from {station_ids[int(ticket[2])].name} to {station_ids[int(ticket[3])].name}, purchased at ${ticket[4]}.")

if show_map:
    map_maker()

if route is not None:
    start, destination = route[0], route[1]
    for station in stations_data:
        if station.name == start:
            start = station
        
        if station.name == destination:
            destination = station
    
    if start == destination:
        print("You're already there")
    else:
        print("Purchase successful")
        unique_id = str(uuid.uuid4())
        new_ticket = Ticket(unique_id, user_id, start, destination)
        price = undergound_network.calculate_price(start, destination)
        ticket_data = [new_ticket.id, user_id, new_ticket.start.id, new_ticket.destination.id, price]
        
        with open("csv_files/tickets.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(ticket_data)