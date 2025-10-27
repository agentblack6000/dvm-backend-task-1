class Line:
    # A metro line needs the stations it goes through
    def __init__(self, name, connections, color):
        self.name = name
        self.connections = connections
        self.color = color

    def is_in_line(self, connection):
        return connection in self.connections

    def get_connections(self):
        connection_names = []
        for connection in self.connections:
            edge = (str(connection.point_a), str(connection.point_b))
            connection_names.append(edge)
        return connection_names