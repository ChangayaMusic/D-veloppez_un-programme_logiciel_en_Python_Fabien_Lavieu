from models.tournament import Tournament
from models.round import Round

class ViewTournament:    
    def create_tournament(self):
        tournament_name = input("Enter tournament's name: ")
        place = input("Enter tournament's place: ")
        nb_rounds = input("How much round (default : 4): ")
        description = input("Enter description: ")

    def tournament_report(self, tournament: Tournament):
        print(tournament.players)
        tournament_name = input("Enter tournament's name: ")
        print(Tournament(tournament_name).__dict__)
        
    def all_players(self):
        tournament_name = input("Enter tournament's name: ")
        print(Tournament(tournament_name.players).__dict__)
        
    def round_matches(self):
        round_name = input("Enter round's name: ")
        print(Round(round_name.matches).__dict__)
        
        
    
    
    