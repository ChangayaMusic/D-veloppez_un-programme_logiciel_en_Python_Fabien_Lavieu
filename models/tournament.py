import datetime
import random
import json
import os

class TournamentManager:
    pass

class Tournament:
    tournaments = []  # List to store tournament objects
    round_list = []  # List to store rounds of the tournament
    
    def __init__(self, tournament_name="", place="", nb_rounds=4, players=[], description='', round_list=None, start_time=None, **kwargs):
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = players
        self.description = description
        self.round_list = round_list
        self.start_time = start_time if start_time else self.get_current_time()
    
    @staticmethod
    def get_current_time():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
   
    @staticmethod
    def load_tournaments_from_file():
        if not os.path.exists('tournaments.json'):
            return []
        with open('tournaments.json', 'r') as file:
            tournaments = json.load(file)
        return tournaments
    
    def to_dict(self):
        return {
            'tournament_name': self.tournament_name,
            'place': self.place,
            'nb_rounds': self.nb_rounds,
            'players': [player.to_dict() for player in self.players],
            'description': self.description,
            'round_list': [r.to_dict() for r in self.round_list] if self.round_list else None,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
    @staticmethod
    def json_encoder(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Player):
            return obj.__dict__
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
    
    @staticmethod
    def save_tournaments_to_file(tournaments):
        tournaments_data = [Tournament(**tournament).to_dict() for tournament in tournaments]
        with open('tournaments.json', 'w') as file:
            json.dump(tournaments_data, file)
            
    @classmethod
    def add_to_database(cls, tournament):
        tournaments = cls.load_tournaments_from_file()
        tournaments.append(tournament.__dict__)
        cls.save_tournaments_to_file(tournaments)
    
    @staticmethod
    def update_tournament(tournaments, tournament):
        for idx, t in enumerate(tournaments):
            if t['tournament_name'] == tournament.tournament_name:
                tournaments[idx] = tournament.__dict__
                break
    
    @staticmethod
    def load_tournament_by_name(tournaments, tournament_name):
        for data in tournaments:
            if data['tournament_name'] == tournament_name:
                tournament = Tournament(**data)
                return tournament
        return None
