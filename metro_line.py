class Line:
    # A metro line needs the stations it goes through
    def __init__(self, name, station_ids):
        self.name = name
        self.stations = station_ids