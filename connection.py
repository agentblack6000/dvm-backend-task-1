class Connection:
    """
    Implements the 'track' or connection between two stations
    """
    def __init__(self, station_one, station_two, distance, cost):
        self.point_a = station_one
        self.point_b = station_two
        self.distance = distance
        self.cost = cost
    