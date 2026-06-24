from database.mongo_connection import collection
from model.soccer_team import SoccerTeam

class SoccerTeamController:
    def save_team(self, team_id, name, won, drawn):

        team = SoccerTeam(team_id, name, won, drawn)

        collection.insert_one(team.to_dict())

        return True