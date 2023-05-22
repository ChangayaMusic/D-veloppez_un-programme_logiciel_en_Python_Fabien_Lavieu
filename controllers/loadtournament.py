<<<<<<< HEAD
from views.viewtournament import LoadTournamentView
from models.tournament import Tournament

class LoadTournamentController : 
    def __init__(self) -> None:
        self.view = LoadTournamentView()
        
    def choose_tournament(self, tournament_name):
        tournament_name = self.view.input_tournament()
        

=======
from views.viewtournament import LoadTournamentView
import os
from models.tournament import Tournament
import json
class LoadTournamentController:
    def __init__(self):
        self.view = LoadTournamentView()
        
    def ask_for_file(self):
        return self.view.ask_for_file()    
    

    def load_tournaments_from_file(self, file_name):
        if not os.path.exists(file_name):
            return None
        with open(file_name, 'r') as file:
            tournaments = json.load(file)
        return tournaments
    

    def load_tournament_by_name(self):
        tournament_name = self.view.input_tournament()
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament['tournament_name'] == tournament_name:
                self.view.tournament_loaded(tournament)
                return tournament
        self.view.tournament_is_not_in_db()

    def file_not_found(self):
        print("File not found")
            
    
    
    def show_tournaments_name_date(self):
        
        tournaments = self.load_tournaments_from_file()

        if tournaments:
            for tournament in tournaments:
                name = tournament["name"]
                date = tournament["date"]
                print(f"Tournament Name: {name}, Date: {date}")
        else:
            print("No tournaments found.")
    
        
>>>>>>> 65e8627d2701bdb0513e83d0c76cf664d7b1c328
