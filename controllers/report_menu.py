<<<<<<< HEAD
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
                
                
                
            
                
                
=======
import os
import json
from views.menu import ReportMenuView
from enum import IntEnum
from models.tournament import Tournament
from controllers.loadtournament import LoadTournamentController
from models.player import Player
from views.viewtournament import LoadTournamentView

class ReportsMenuOptions(IntEnum):
    UNASSIGNED = -1
    ALL_PLAYERS = 0
    TOURNAMENT_LIST = 1
    TOURNAMENT_DATE_NAME = 2
    TOURNAMENT_PLAYERS = 3
    TOURNAMENT_ROUNDS_MATCHES = 4
    EXIT = 5

class ReportsMenuController:
    def __init__(self):
        self.load_tournament_controller = LoadTournamentController()
        self.view = ReportMenuView()
        self.all_players = None
        self.tournament_list = None
        self.tournament_date_name = None
        self.tournament_players = None
        self.rounds_matches = None

    def start_loop(self):
        option_selected = ReportsMenuOptions.UNASSIGNED
        while option_selected != ReportsMenuOptions.EXIT:
            option_selected = int(self.view.select_report())

            if option_selected == ReportsMenuOptions.ALL_PLAYERS:
                if not self.all_players:
                    self.all_players = Player.load_players_from_json()
                self.view.display_all_players(self.all_players)

            if option_selected == ReportsMenuOptions.TOURNAMENT_LIST:
                if not self.tournament_list:
                    file_name = self.load_tournament_controller.ask_for_file()
                    if file_name is None:
                        LoadTournamentView.file_not_found()
                    elif not os.path.exists(file_name):
                        LoadTournamentView.file_not_found()
                    else:
                        self.tournament_list = self.load_tournament_controller.load_tournaments_from_file(file_name)
                        if self.tournament_list is None:
                            LoadTournamentView.file_not_found()
                        else:
                            LoadTournamentView.show_tournaments_list

            if option_selected == ReportsMenuOptions.TOURNAMENT_DATE_NAME:
                if not self.tournament_list:
                    file_name = self.load_tournament_controller.ask_for_file()
                    if file_name is None:
                        LoadTournamentView.file_not_found()
                    elif not os.path.exists(file_name):
                        LoadTournamentView.file_not_found()
                    else:
                        self.tournament_list = self.load_tournament_controller.load_tournaments_from_file(file_name)
                        if self.tournament_list is None:
                            LoadTournamentView.file_not_found()
                        else:
                            LoadTournamentView.show_tournaments_name_date(self.tournament_list)

            if option_selected == ReportsMenuOptions.TOURNAMENT_PLAYERS:
                if not self.tournament_players:
                    tournament_name = LoadTournamentView.input_tournament_name()
                    self.tournament_players = self.load_tournament_controller.load_tournament_by_name(tournament_name)
                self.view.display_tournament_players(self.tournament_players)

            if option_selected == ReportsMenuOptions.TOURNAMENT_ROUNDS_MATCHES:
                if not self.rounds_matches:
                    tournament_name = LoadTournamentView.input_tournament_name()
                    self.rounds_matches = self.load_tournament_controller.load_tournament_by_name(tournament_name)
                self.view.display_tournament_rounds_matches(self.rounds_matches)
>>>>>>> 65e8627d2701bdb0513e83d0c76cf664d7b1c328
