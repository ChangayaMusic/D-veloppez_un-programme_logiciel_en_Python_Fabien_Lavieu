from models.player import Player

class AddPlayerView:
    def input_first_name(self):
        return input("What is your first name ? ")
    
    def input_last_name(self):
        return input("What is your last name ? ")
    
    def input_identification(self):
        return input("What is your ID ? ")
    
    def display_identification_error(self):
        print("Invalid identification")

    def print_player_added(self, player):
        print(f"Player added: { player }")
        
    def bd_validation(self, player):
        print(f"Player added to DataBase: { player }")
        
    def already_in_db(self,player):
        print(f"Player already in DataBase: { player }")
        


