class Station:
    # A station should have its id and name
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return self.name