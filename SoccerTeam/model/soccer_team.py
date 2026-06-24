class SoccerTeam:
    def __init__(self, team_id, name, matches_won, matches_drawn):
        self.team_id = team_id
        self.name = name
        self.matches_won = matches_won
        self.matches_drawn = matches_drawn

    def calculate_points(self):
        return (self.matches_won * 3) + self.matches_drawn
    def to_dict(self):
        return {
        "team_id": self.team_id,
        "name": self.name,
        "matches_won": self.matches_won,
        "matches_drawn": self.matches_drawn,
        "points": self.calculate_points()
    }
