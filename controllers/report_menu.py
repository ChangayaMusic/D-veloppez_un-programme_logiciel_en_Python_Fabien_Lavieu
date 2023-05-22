import os
import json
from views.menu import ReportMenuView
from enum import IntEnum
from models.tournament import Tournament
from controllers.load_tournament import LoadTournamentController
from models.player import PlayerManager
from views.view_tournament import LoadTournamentView

class ReportsMenuOptions(IntEnum):
    UNASSIGNED = -1
    ALL_PLAYERS = 0
    TOURNAMENT_LIST = 1
    TOURNAMENT_DATE_NAME = 2
    TOURNAMENT_PLAYERS = 3
    TOURNAMENT_ROUNDS_MATCHES = 4
    EXIT = 5

class ReportsMenuController:
    def __init__(self, player_manager):
        self.load_tournament_controller = LoadTournamentController()
        self.view = ReportMenuView()
        self.player_manager = player_manager
        self.tournament_list = None
        self.tournament_date_name = None
        self.tournament_players = None
        self.rounds_matches = None

    def start_loop(self):
        option_selected = ReportsMenuOptions.UNASSIGNED
        while option_selected != ReportsMenuOptions.EXIT:
            option_selected = int(self.view.select_report())

            if option_selected == ReportsMenuOptions.ALL_PLAYERS:
                players = PlayerManager.load_players_from_json()
                self.view.display_all_players(players)

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
