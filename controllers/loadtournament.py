from views.viewtournament   import  LoadTournamentView
from models.tournament import Tournament
import json
class LoadTournamentController : 
    def __init__(self) -> None:
        self.view = LoadTournamentView()
        
    
        
    def load_tournaments_from_file(self):
            with open('tournaments.json', 'r') as file:
                tournaments = json.load(file)
            return tournaments
        
    def load_tournament_by_name(self, tournament_name):
        tournament_name = self.view.input_tournament()
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament['tournament_name'] == tournament_name:
                return tournament
            else:
                self.view.tournament_is_not_in_db()
        

