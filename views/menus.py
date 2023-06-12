# from views.viewplayer import ViewPlayer
from models.tournament import Tournament

class MainMenuView:
    def display_welcome(self):
        print("Welcome in the chess tournament manager !")

    def select_option(self):
        return input(
            "Please choose an option to continue:\n"
            "0: Create a new player\n"
            "1: Create a new tournament\n"
            "2: Continue an existing tournament\n"
            "3: Show reports\n"
            "4: Exit\n"
            "Your choice ? "
        )

class ReportMenuView:
    def select_report(self):
        return input(
            "Please choose an option to continue:\n"
            "0: All players by name (A-Z)\n"
            "1: Tournament's list\n"
            "2: Tournament's name and date \n"
            "3: Tournament's players by name (A-Z)\n"
            "4: All tournament's rounds and matches\n"
            "5: Main Menu\n"
            "Your choice ? "
        )

    def display_players(self):
        print(Tournament.players)
    
    def tournaments_names(self,tournament):
        for name in Tournament.tournament_names:
            print(name)
        
    def names_and_dates(self,tournament):
        print(Tournament.tournament_dict)
        
    def display_all_players(self, players):
        print("**********************")
        print("All players by name : ")
        print("**********************")
        sorted_players = sorted(players, key=lambda player: player.last_name)
        for player in sorted_players:
            print(player)
            print("**********************")
    @staticmethod        
    def display_tournament_players():
        print("**********************")
        print("Tournament's players by name : ")
        print("**********************")
        
    def player_infos(player):
        print(f"Name:{player['first_name']} {player['last_name']} Id: {player['identification']} Points: {player['points']}")
        ("**************************************")
        
              
    @staticmethod
    def show_tournaments_list(tournaments):
        print("**************************************")
        print('Tournament name || Start time || place')
        print("**************************************")
        for tournament in tournaments:
            print(f"{tournament.tournament_name}||{tournament.start_time}|| {tournament.place}||")
            print("**************************************")
    def show_tournaments(tournament):
        print("**************************************")
        print('Tournament name || Start time || place')
        print("**************************************")  
        print(f"{tournament.tournament_name}||{tournament.start_time}|| {tournament.place}||")         
    
    def rounds(round):
        print(f"{round.name}")
    
    def matches(player1,player2):
        print(f"Match: {player1.name}{player1.points}  vs {player1.name} {player2.points}")
            
    
    
class TournamentActionsMenu:
    def select_action(self):
        return input(
                "Please choose an option to continue:\n"
                "0: Add player(s) to a tournament\n"
                "1: Start tournament\n"
                "2: End tournament\n"
                "3: Return to menu\n"
                "Your choice ? "
            )
      
    def show_players(self,players):
        for player in players:
            print(player.last_name,player.identification)
            pass
    
    def get_players_ids(self,players_to_add):
        ids = input("Enter player's ids (separated by commas): ").split(",")
        for i in ids:
            players_to_add.append(i)
        return players_to_add
    
    def data_error(self):
        print('Data error')
        
    def tournaments_updated(self):
        print('Tournaments updated')
        
    def get_match_winner(self, player1, player2):
        
        print(f"Match: {player1['first_name']} {player1['last_name']} vs {player2['first_name']} {player2['last_name']}")
        print(f"1. {player1['first_name']} {player1['last_name']}")
        print(f"2. {player2['first_name']} {player2['last_name']}")
        print("3. Draw")
        return int(input("Select the winner (1-3): "))

    def wrong_result():
        print('Wrong inpout : only 1,2,3 are allowed')
        
    
 
        
    
