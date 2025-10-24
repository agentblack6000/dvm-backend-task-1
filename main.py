from argparse import ArgumentParser
import csv

# Read exisiting data
stations = []
station_names = {}
with open("csv_files/stations.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    for station_data in reader:
        station_names[station_data[0]] = station_data[1]
        stations.append(station_data)

user_names = []
users = []
with open("csv_files/users.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    for user_data in reader:
        user_names.append(user_data[1])
        users.append(user_data)

tickets = []
with open("csv_files/tickets.csv", "r") as file:
    reader = csv.reader(file, delimiter=',')
    for ticket_data in reader:
        tickets.append(ticket_data)

# Configure ArgumentParser
parser = ArgumentParser(prog="Metro Ticket Purchasing System", 
                                 description="A metro ticket purchasing system")

parser.add_argument("--user", required=True, choices=user_names)
parser.add_argument("-s", "--station", action='store_true', help="Shows a list of all available stations")
parser.add_argument("-p", "--purchase", nargs=2, choices=station_names.values(),
                    help="Purchase a ticket from station to station", metavar=('station_A', 'station_B'))
parser.add_argument("-v", "--view", action='store_true', help="View all purchased tickets.")

# Get the command-line arguments the user provided
args = parser.parse_args()
show_stations = args.station
show_tickets = args.view
route = args.purchase

user_name = args.user

# Get user id from the database
user_id = None
for user in users:
    if user_name == user[1]:
        user_id = user[0]

if show_stations:
    print("The list of stations available are:")
    for station in stations:
        print(station)

if show_tickets:
    for ticket in tickets:
        if ticket[1] == user_id:
            print(f"{user_name} has a ticket from {station_names[ticket[2]]} to {station_names[ticket[3]]}, purchased at ${ticket[4]}.")
