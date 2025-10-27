class Line:
    # A metro line needs the stations it goes through
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
    
    def is_in_line(self, connection):
        return connection in self.connections