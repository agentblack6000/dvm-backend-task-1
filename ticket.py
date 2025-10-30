from railway_network import undergound_network

class Ticket:
    """
    Creates a ticket with the provided ids, start and end Stations
    Prints user help for the journey
    """
    def __init__(self, id, user_id, start_station, destination):
        self.id = id
        self.user = user_id
        self.start = start_station
        self.destination = destination
        self.price = undergound_network.calculate_price(start_station, destination)
        self.assist()
    
    def assist(self):
        route = list(undergound_network.find_shortest_path(self.start, self.destination))
        lines = undergound_network.lines

        current_line = None
        for line in lines:
            if line.is_in_line(route[0]):
                current_line = line
                break
        
        print(f"Start at {self.start.name}, use the {current_line.name}")
        if current_line == None:
            print("problem")

        change = False
        for track in route:
            if not current_line.is_in_line(track):
                change = True
                old_line = current_line
                for line in lines:
                    if line.is_in_line(track):
                        current_line = line
                
                print(f"Reach {track.point_a} using {old_line.name}")
                print(f"Changing from {old_line.name} at {track.point_a} to {current_line.name} to reach {track.point_b}")
        
        if not change:
            print(f"Reach {self.destination.name} using {current_line.name}")