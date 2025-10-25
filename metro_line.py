class Line:
    # A metro line needs the stations it goes through
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections