from views.viewtournament import LoadTournamentView
from models.tournament import Tournament

class LoadTournamentController : 
    def __init__(self) -> None:
        self.view = LoadTournamentView()
        
    def choose_tournament(self, tournament_name):
        tournament_name = self.view.input_tournament()
        

