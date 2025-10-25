from connection import Connection
from metro_line import Line
from creator import stations_data

class Network:
    def __init__(self, lines: list):
        self.lines = lines

    def find_shortest_path(start, destination):
        pass


# Creates the railway network
one_two = Connection(stations_data[0], stations_data[1], 5)
two_three = Connection(stations_data[1], stations_data[2], 5)
three_four = Connection(stations_data[2], stations_data[3], 5)
three_five = Connection(stations_data[2], stations_data[4], 5)
three_six = Connection(stations_data[2], stations_data[5], 5)
two_seven = Connection(stations_data[1], stations_data[6], 5)
six_one = Connection(stations_data[5], stations_data[0], 5)


blue_line = Line("Blue Line", [one_two, two_three, three_four])
red_line = Line("Red Line", [three_six, six_one])
green_line = Line("Green Line", [one_two, two_three, three_five])
yellow_line = Line("Yello Line", [two_seven])


undergound_network = Network([blue_line, red_line, green_line, yellow_line])
