class Station:
    """
    Creates a Station, which has its own unique id and name
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return self.name