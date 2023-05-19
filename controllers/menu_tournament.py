from views.viewtournament import AddTournamentView
from models.tournament import Tournament
from tinydb import TinyDB, Query

class AddTournamentController:

    def __init__(self):
        self.view = AddTournamentView()
        
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
            return description
          
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
        description = self.validate_descriptions
        
        tournament = Tournament(tournament_name=tournament_name, place=place, description = description)
        
        
    
        Tournament.check_if_in_database(tournament)
        if not result:
            Tournament.add_to_database(tournament)
            self.view.print_tournament_added(tournament)
        else:
            self.view.already_in_db
        
        return tournament
        
class LoadTournamentController:
    
    def __init__(self):
        self.view = AddTournamentView()
        
    def load_tournament(self, tournament, tournament_name):
        
        db = TinyDB('tournaments.json')
        Tournament.check_if_in_database(tournament)
        if result:
            tournament_data = result[0]
            tournament = Tournament(**tournament_data)
            self.view.load_tournament(tournament)
        else:
             self.view.tournament_is_not_in_db(tournament)
    
    
        

    
        
        
        
        