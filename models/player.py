import json
from datetime import datetime
from models.tournament import Tournament

class Player:
    players = []  # List to store player objects
    
    def __init__(self, last_name, first_name, birth_date, identification,
                 points=0, opponents=[], tournament_score=0, rank=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.identification = identification
        self.points = points
        self.rank = rank
        self.opponents = opponents
        self.tournament_score = tournament_score
    
    def __repr__(self) -> str:
        return f"{self.last_name} {self.birth_date} - {self.identification}"
    
    @staticmethod
    def load_players_from_json():
        try:
            with open('players.json', 'r') as file:
                players_data = json.load(file)
                for player_data in players_data:
                    player = Player(**player_data)
                    Player.players.append(player)
        except FileNotFoundError:
            Player.players = []
    
    @staticmethod
    def save_players_to_json():
        players_data = [player.__dict__ for player in Player.players]
        with open('players.json', 'w') as file:
            json.dump(players_data, file)
    
    def check_if_in_db(self):
        for player in Player.players:
            if player.identification == self.identification:
                return True
        return False
    
    def add_player_to_db(self):
        if not self.check_if_in_db():
            Player.players.append(self)
            Player.save_players_to_json()
