import re
from models/tournament import Tournament

def class ViewPlayer:
    
    
    
    def create_player(self):
       
        last_name_input = input("Please enter your last name: ")
        surname_input = input("Please enter your surname: ")
        birth_date_input = input("Please enter your birth date (YYYY-MM-DD): ")
        
        while identification_input is None:
            
            identification_input = input("Please enter your identification: ")
            
            regex = r"^[a-zA-Z]{2}\d{4}$"
            
            if re.match(regex, identification_input):
                continue
            else:
                print("This is not a correct ID.")
                identification_input = None
            
        
    def show_player(self):
        
        identification_input = input("Please enter the player's identification: ")
        #look for player with controllers
       
        for k, v in Tournament().players.items():
            if v == identification_input:
                print(k) 
            else : "Indentification number is not found"
                
        
    def show_all_players(self, all_players = {}):
        
        all_players = Tournaments.players
        print(all_players.__dict__)
        
    
        
    
        
        
        
        
        
