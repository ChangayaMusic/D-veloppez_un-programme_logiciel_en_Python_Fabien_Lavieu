from views.menu import ReportMenuView
from enum import IntEnum
from models.tournament import Tournament
from controllers.menu_tournament import LoadTournamentController
from models.player import Player
from views.viewtournament   import LoadTournamentView
from controllers.loadtournament import LoadTournamentController
import json


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
        self.show_tournaments_list=None
        self.all_players=None
        self.show_tournaments_date_name=None
        self.tournament_players = None
        self.rounds_matches = None
        
    
  
        
    def start_loop(self):
        option_selected = ReportsMenuOptions.UNASSIGNED
        while option_selected != ReportsMenuOptions.EXIT:
            option_selected = int(self.view.select_report())
            
            if option_selected == ReportsMenuOptions.ALL_PLAYERS:
                if not self.all_players:
                    self.all_players = Player.load_players_from_json()
                self.view.display_all_players(self)
                
            if option_selected == ReportsMenuOptions.TOURNAMENT8_LIST:
                if not self.show_tournaments_list:
                    self.show_tournaments_list = LoadTournamentController.load_tournaments_from_file()
                self.view.show_tournaments_list()    
                
                
            if option_selected == ReportsMenuOptions.TOURNAMENT8_DATE_NAME:
                if not self.show_tournaments_date_name:
                    self.show_tournaments_date_name = Tournament.get_tournaments_names()
                self.view.names_and_dates()
                
            if option_selected == ReportsMenuOptions.TOURNAMENT8_PLAYERS:
                if not self.tournament_players:
                    self.tournament_players = LoadTournamentController()
                Tournament.sort_by_name(self.tournament)
                self.view.display_players(self.tournament)
                
            if option_selected == ReportsMenuOptions.TOURNAMENT_ROUNDS_MATCHES:
                if not self.rounds_matches:
                    self.rounds_matches = LoadTournamentController()
                
                
                
            
                
                