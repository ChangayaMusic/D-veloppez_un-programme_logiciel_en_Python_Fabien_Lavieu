from models.tournament import Tournament
from models.round import Round

class AddTournamentView:    
        
    def input_tournament_name(self):
        tournament_name = input("Enter tournament's name: ")
        return tournament_name
    
    def input_tournament_place(self):
        place = input("Enter tournament's place: ")
        return place
        
    def input_tournament_rounds(self, nb_rounds=4):
        
        nb_rounds = input("How much rounds (default : 4): ")
        return nb_rounds
    
    def input_tournament_description(self):   
        
        description = input("Enter description: ")
        return description
    
    def print_tournament_added(self, tournament):
        print(f"Tournament added: { tournament }")
        
    def display_nb_rounds_errors(self):
        print("Invalid nb_rounds")
    
    def empty_tournament_description(self,response):
        response = input("Are you sure you want to leave it empty? (yes/no) ")
        
        
        if response.lower() == "yes":
            print("You chose yes.")
        else :
            self.input_tournament_descriptions()
            
        return response
    def bd_validation(self, tournament):
        print(f"Tournament added to DataBase: { tournament }")
        
    def already_in_db(self,tournament):
        print(f"Tournament already in DataBase: { tournament }")
    
    def tournament_is_not_in_db(self,tournament):
        print(f"Tournament's name does not exist in DataBase: { tournament }")
    
    def input_tournament_to_load(self):
        tournament_name = input("Enter tournament's name to load: ")
        return tournament_name
    
    def tournament_loaded(self,tournament):
        print(f"Tournament loaded from DataBase: { tournament }")
        
    
class LoadTournamentView:
    
    def input_tournament(self,tournament_name):
        tournament_name = input("Enter the name of the tournament you want to load")
        return tournament_name
    
    def tournaments_names(self,tournament):
        for name in tournament.tournament_names:
            print(name)
        
    
        
    
    
    