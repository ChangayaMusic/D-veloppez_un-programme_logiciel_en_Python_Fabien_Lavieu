import json
from datetime import datetime, date

class PlayerManager:
    def __init__(self):
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
        self.players = []
        try:
            with open('players.json', 'r') as file:
                players_data = json.load(file)
                for player_data in players_data:
                    player = Player(**player_data)
                    self.players.append(player)
        except FileNotFoundError:
            # Handle the case when players.json doesn't exist
            self.players = []
        return self.players

    def save_players_to_json(self):
        players_data = [player.to_dict() for player in self.players]
        with open('players.json', 'w') as file:
            json.dump(players_data, file, default=Player.json_encoder)

    def find_player_by_identification(self, identifier):
        return [player for player in self.players if player.identification == identifier]

    def add_points_to_player(player_id, points):
        # Load player data from player.json
        with open('players.json', 'r') as file:
            players = json.load(file)

        # Find the player by ID and update the points
        for player in players:
            if player['identification'] == player_id:
                player['points'] += points
                break

        # Save the updated player data back to player.json
        with open('players.json', 'w') as file:
            json.dump(players, file, indent=4)
class Player:
    def __init__(self, last_name, first_name, birth_date, identification,
                 points=0, opponents=[], total_points=0, rank=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.identification = identification
        self.points = points
        self.rank = rank
        self.opponents = opponents
        self.total_points = total_points

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.birth_date} - {self.identification}"

    @staticmethod
    def json_encoder(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Player):
            return obj.__dict__
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def to_json(self):
        return json.dumps(self, default=self.json_encoder)

    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': str(self.birth_date),
            'identification': self.identification,
            'points': self.points,
            'rank': self.rank,
            'opponents': self.opponents,
            'total_points': self.total_points
        }