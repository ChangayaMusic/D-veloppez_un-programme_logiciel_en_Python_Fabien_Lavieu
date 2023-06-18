import datetime
import json
import os
from models.round import Round


class Tournament:
    tournaments = []  # List to store tournament objects
    rounds = []  # List to store rounds of the tournament

    def __init__(self, tournament_name="", place="", nb_rounds=4, players=[], description='', rounds=[], start_time=None, **kwargs):
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = players
        self.description = description
        self.rounds = rounds
        self.start_time = start_time if start_time else self.get_current_time()

    @staticmethod
    def get_current_time():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'tournament_name': self.tournament_name,
            'place': self.place,
            'nb_rounds': self.nb_rounds,
            'players': [player.to_dict() for player in self.players],  # Include player data
            'description': self.description,
            'rounds': self.rounds,
            'start_time': self.start_time,
            'end_time': self.end_time
        }

    @staticmethod
    def json_encoder(obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


class TournamentManager:
    def __init__(self):
        self.tournaments = self.load_tournaments_from_file()
        self.tournament_name = ''
        self.tournament = None

    def save_tournaments_to_file(self):
        tournaments_data = [tournament.to_dict() for tournament in self.tournaments]  # Convert tournaments to dictionaries
        with open('tournaments.json', 'w') as file:
            json.dump(tournaments_data, file, default=Tournament.json_encoder, indent=4)  # Use custom JSON encoder

    def load_tournament_by_name(self, tournament_name):
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament.tournament_name == tournament_name:
                self.tournament = tournament  # Assign the tournament to self.tournament
                return tournament
        return None

    def load_tournaments_from_file(self):
        if not os.path.exists('tournaments.json'):
            return []
        with open('tournaments.json', 'r') as file:
            tournaments_data = json.load(file)

        self.tournaments = []
        for data in tournaments_data:
            tournament = Tournament(**data)
            tournament.rounds = [Round(**round_data) for round_data in data['rounds']]
            self.tournaments.append(tournament)

        return self.tournaments
    
    def add_player_to_tournament(self, tournament_name, player):
        for tournament in self.tournaments:
            if tournament.tournament_name == tournament_name:
                tournament.players.append(player)
                self.update_tournaments_file()
                break

            else:
                print("no tournament RRrrrrRRRRRRrRRRrRR")
    def update_tournament_players(tournament_players):
    # Load player data from players.json
        with open('players.json', 'r') as file:
            players = json.load(file)

        # Iterate through tournament players and update their information
        for tournament_player in tournament_players:
            for player in players:
                if player['identification'] == tournament_player['identification']:
                    player['opponents'] = tournament_player['opponents']  # Update oppenonents
                    player['total_points'] = player['total_points'] + tournament_player['points']  # Update total points
                    
                    break

            with open('players.json', 'w') as file:
                json.dump(players, file, indent=4)
                
    def add_player_to_tournament(self, tournament_name, player):
        for tournament in self.tournaments:
            if tournament.tournament_name == tournament_name:
                tournament.players.append(player)

                break

            else:
                print("no tournament RRrrrrRRRRRRrRRRrRR")   
    def update_tournaments_file(self):
        tournaments_data = []
        with open('tournaments.json', 'r') as file:
            tournaments_data = json.load(file)

        for data in tournaments_data:
            if data['tournament_name'] == self.tournament.tournament_name:
                # Update the tournament object
                data.update(self.tournament.to_dict())
                break

        with open('tournaments.json', 'w') as file:
            json.dump(tournaments_data, file, indent=4, default=Tournament.json_encoder)

    def update_players_points(self):
        with open('players.json', 'r') as players_file:
            players_data = json.load(players_file)
        for t_player in self.tournament.players:
            for player in players_data:
                if t_player['identification']== player['identification']:
                    player['total_points'] += t_player['points']
                    player['opponents'] = t_player['opponents']
        players_data.sort(key=lambda player: player['points'], reverse=True)  # Sort players by points in descending order
        
        for i, player in enumerate(players_data, start=1):
            player['rank'] = i  # Update the rank of each player based on their position
                 
        with open('players.json', 'w') as players_file:
            json.dump(players_data, players_file, indent=4)    
