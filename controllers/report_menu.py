from views.menu import ReportMenuView
from enum import IntEnum
from models.tournament import Tournament
from controllers.menu_tournament import LoadTournamentController
from models.player import Player
from views.viewtournament import ViewTournament, LoadTournamentView

class ReportsMenuOptions(IntEnum):
    UNASSIGNED = -1
    ALL_PLAYERS = 0
    TOURNAMENT8_LIST = 1
    TOURNAMENT8_DATE_NAME = 2
    TOURNAMENT8_PLAYERS = 3
    TOURNAMENT_ROUNDS_MATCHES = 4
    EXIT = 5
    
class ReportsMenuController:
    def __init__(self) -> None:
        self.tournament = Tournament()
        self.view = ReportMenuView()
        
    def start_loop(self):
        option_selected = ReportMenuView.UNASSIGNED
        while option_selected != ReportMenuView.EXIT:
            option_selected = int(self.view.select_option())
            
            if option_selected == ReportMenuView.ALL_PLAYERS:
                if not self.all_players:
                    self.all_players = Tournament.all_player_by_name(self)
                self.view.display_all_players(self)
                
            if option_selected == ReportMenuView.TOURNAMENT8_LIST:
                if not self.show_tournaments_list:
                    self.show_tournaments_list = Tournament.get_tournaments_names
                LoadTournamentView.tournaments_names()
                
            if option_selected == ReportMenuView.TOURNAMENT8_DATE_NAME:
                if not self.show_tournaments_date_name:
                    self.show_tournaments_date_name = Tournament.get_tournaments_names
                self.view.names_and_dates()
                
            if option_selected == ReportMenuView.TOURNAMENT8_PLAYERS:
                if not self.tournament_players:
                    self.tournament_players = LoadTournamentController()
                Tournament.sort_by_name(self.tournament)
                self.view.display_players(self.tournament)
                
            if option_selected == ReportMenuView.TOURNAMENT_ROUNDS_MATCHES:
                if not self.rounds_matches:
                    self.rounds_matches = LoadTournamentController()
                
                
                
            
                
                