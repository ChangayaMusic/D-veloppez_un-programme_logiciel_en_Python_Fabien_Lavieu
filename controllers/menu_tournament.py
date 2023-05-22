import json
from views.viewtournament import AddTournamentView
from models.tournament import Tournament

class AddTournamentController:
    def __init__(self):
        self.view = AddTournamentView()
        self.file_name = 'tournaments.json'
        
    def validate_nb_rounds(self, nb_rounds):
        if nb_rounds.isdigit():
            return nb_rounds
        else:
            self.view.display_nb_rounds_errors()
    
    def validate_descriptions(self, description, response): 
        if description is None:
            self.view.empty_tournament_description()
        elif response.lower() == "yes":
            return description
        elif response.lower() == "no":
            self.view.input_tournament_description()
            return self.view.get_user_input()
          
    def add_new_tournament(self):
        tournament_name = None
        place = None
        nb_rounds = 4
        description = None
        while not tournament_name:
            tournament_name = self.view.input_tournament_name()
        while not place:
            place = self.view.input_tournament_place()
        description = self.view.input_tournament_description()
        description = self.validate_descriptions(description, response="yes")
        
        tournament = Tournament(tournament_name=tournament_name, place=place, description=description)
        
        if not self.check_if_tournament_exists(tournament):
            self.add_tournament_to_db(tournament)
            self.view.print_tournament_added(tournament)
        else:
            self.view.already_in_db()
        
        return tournament
    
    def check_if_tournament_exists(self, tournament):
        tournaments = self.load_tournaments_from_file()
        return any(t['tournament_name'] == tournament.tournament_name for t in tournaments)
    
    def add_tournament_to_db(self, tournament):
        tournaments = self.load_tournaments_from_file()
        tournaments.append(tournament.__dict__)
        self.save_tournaments_to_file(tournaments)
    
    def load_tournaments_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_tournaments_to_file(self, tournaments):
        with open(self.file_name, 'w') as file:
            json.dump(tournaments, file)

class LoadTournamentController:
    def __init__(self):
        self.view = AddTournamentView()
        self.file_name = 'tournaments.json'
        
    def load_tournament(self, tournament_name):
        tournaments = self.load_tournaments_from_file()
        result = [t for t in tournaments if t['tournament_name'] == tournament_name]
        if result:
            tournament_data = result[0]
            tournament = Tournament(**tournament_data)
            self.view.load_tournament(tournament)
        else:
            self.view.tournament_is_not_in_db(tournament_name)
    
    def load_tournaments_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
