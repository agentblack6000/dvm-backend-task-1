from connection import Connection
from metro_line import Line
from creator import stations_data

class Network:
    """
    Implements the railway network
    Uses Dijkstra's algorithm to find the shortest path between two Stations
    """
    def __init__(self, lines: list):
        self.lines = lines

    def find_shortest_path(self, start, destination) -> list:
        graph = {}
        connections = []
        for line in self.lines:
            for connection in line.connections:
                point_a = str(connection.point_a)
                point_b = str(connection.point_b)

                if point_a not in graph:
                    graph[point_a] = {}
                
                if point_b not in graph:
                    graph[point_b] = {}

                graph[point_a][point_b] = connection.distance
                graph[point_b][point_a] = connection.distance
                connections.append(connection)
        
        # Each node is a station
        distances = {node: float("inf") for node in graph}
        distances[start.name] = 0
        previous = {node: None for node in graph}
        visited = set()

        while len(visited) < len(graph):
            # Find unvisited node with minimum distance
            min_distance = float('inf')
            current_node = None
            for node in graph:
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    current_node = node

            if current_node is None:  # No reachable unvisited nodes left
                break

            visited.add(current_node)

            # Relax neighbors
            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_node
        
        path_taken = []
        current_node = destination.name
        while current_node is not None:
            path_taken.append(current_node)
            current_node = previous[current_node]
        path_taken.reverse()
        
        route = set()
        ordered_route = []
        for track in connections:
            if str(track.point_a) in path_taken and str(track.point_b) in path_taken:
                route.add(track)

                if track in route and (track not in ordered_route):
                    ordered_route.append(track)
        
        return ordered_route

    def calculate_price(self, start, destination):
        shortest_path = self.find_shortest_path(start, destination)
        price = 0
        for connection in shortest_path:
            price += connection.cost
        
        return price

    def graph_connections(self):
        connections = set()
        for line in self.lines:
            for connection in line.connections:
                connections.add(connection)
        
        return connections

# Creates the railway network
one_two = Connection(stations_data[0], stations_data[1], 5, 5)
two_three = Connection(stations_data[1], stations_data[2], 5, 5)
three_four = Connection(stations_data[2], stations_data[3], 5, 5)
three_five = Connection(stations_data[2], stations_data[4], 5, 5)
three_six = Connection(stations_data[2], stations_data[5], 5, 5)
two_seven = Connection(stations_data[1], stations_data[6], 5, 5)
six_one = Connection(stations_data[5], stations_data[0], 5, 5)


blue_line = Line("Blue Line", [one_two, two_three, three_four], "blue")
red_line = Line("Red Line", [three_six, six_one], "red")
green_line = Line("Green Line", [one_two, two_three, three_five], "green")
yellow_line = Line("Yellow Line", [one_two, two_seven], "yellow")


undergound_network = Network([blue_line, red_line, green_line, yellow_line])
