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

# class ViewPlayer:    
#     def create_player(self):
#         last_name_input = input("Please enter your last name: ")
#         surname_input = input("Please enter your surname: ")
#         birth_date_input = input("Please enter your birth date (YYYY-MM-DD): ")
#         if birth_date_input:
#             identification_input = input("Please enter your identification: ")

#     def show_player(self):
#         identification_input = input("Please enter the player's identification: ")
#         #look for player with controllers
#         # player_to_show = #Plazer(#)
#         # print(player_to_show.__dict__)
        
#     def show_all_players(self, all_players = {}):
#         all_players = Tournament.players
#         print(all_players.__dict__)
