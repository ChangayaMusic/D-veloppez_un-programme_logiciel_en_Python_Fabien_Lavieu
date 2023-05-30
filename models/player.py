import json
from datetime import datetime, date

class PlayerManager:
    def __init__(self) -> None:
        self.players = self.load_players_from_json()
            
    def add(self, player):
        self.players.append(player)
        self.save_players_to_json()

    def check(self, player):
        for db_player in self.players:
            if player.identification == db_player.identification:
                return True
        return False

    def load_players_from_json(self):
        players = []

        
        with open('players.json', 'r') as file:
            players_data = json.load(file)
    
        for player_data in players_data:
            player = Player(**player_data)
            players.append(player)

        return players
    
    def save_players_to_json(self):
        players_data = [player.to_dict() for player in self.players]
        with open('players.json', 'w') as file:
            json.dump(players_data, file)
            
    def find_player_by_identification(self, id,players,found_players=[]):
        for player in players:
            if player.identification == id:
                found_players.append(player)
        return found_players
           
        

class Player:
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
        return f"{ self.first_name } { self.last_name } { self.birth_date } - { self.identification }"
    
    @staticmethod
    def json_encoder(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
    
    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': str(self.birth_date),
            'identification': self.identification,
            'points': self.points,
            'rank': self.rank,
            'opponents': self.opponents,
            'tournament_score': self.tournament_score
        }
