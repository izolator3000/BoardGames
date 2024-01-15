class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.points = 0

    def set_name(self, name):
        self.name = name

    def add_points(self, points):
        self.points += points
