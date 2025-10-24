class Ticket:
    # Tickets need to have their price (calculate), start and end points, and the user they're linked with
    def __init__(self, id, user_id, start_station_id, destination_id):
        self.id = id
        self.user = user_id
        self.start = start_station_id
        self.destination = destination_id
        self.price = self.__calculate_price(start_station_id, destination_id)
    
    def __calculate_price(start_station_id, destination_id):
        pass