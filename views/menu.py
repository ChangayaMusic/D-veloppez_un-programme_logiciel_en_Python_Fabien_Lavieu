# from views.viewplayer import ViewPlayer
from models.tournament import Tournament
from models.round import Round

class MainMenuView:
    def display_welcome(self):
        print("Welcome in the chess tournament manager !")

    def select_option(self):
        return input(
            "Please choose an option to continue:\n"
            "0: Create a new player\n"
            "1: Create a new tournament\n"
            "2: Create a new round\n"
            "3: Continue an existing tournament\n"
            "4: Show reports\n"
            "5: Exit\n"
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
        
    def display_all_players(self,tournament):
        for player in Tournament.sorted_players:
            print(player['name'])
            
    def rounds_matches(self,tournament):
        print()
