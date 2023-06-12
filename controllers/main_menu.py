from enum import IntEnum
from views.menus import MainMenuView
from models.player import PlayerManager
from models.tournament import TournamentManager
from controllers.menu_player import AddPlayerController
from controllers.add_tournament import AddTournamentController, LoadTournamentController
from controllers.report_menu import ReportsMenuController
from controllers.tournament_menu import ActionMenuController


class MainMenuOptions(IntEnum):
    UNASSIGNED = -1
    NEW_PLAYER = 0
    NEW_TOURNAMENT = 1
    LOAD_TOURNAMENT = 2
    SHOW_REPORTS = 3
    EXIT = 4


class MainMenuController:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournaments = TournamentManager.load_tournaments_from_file(self)
        self.tournament_manager = TournamentManager()

        self.add_player_controller = None
        self.add_tournament_controller = None
        self.add_round_controller = None
        self.load_tournament_controller = None
        self.show_report_controller = None

        self.view = MainMenuView()
        self.view.display_welcome()

    def start_loop(self):
        option_selected = MainMenuOptions.UNASSIGNED
        while option_selected != MainMenuOptions.EXIT:
            option_selected = int(self.view.select_option())
            if option_selected == MainMenuOptions.NEW_PLAYER:
                if not self.add_player_controller:
                    self.add_player_controller = AddPlayerController(self.player_manager)
                _ = self.add_player_controller.add_new_player()
            elif option_selected == MainMenuOptions.NEW_TOURNAMENT:
                if not self.add_tournament_controller:
                    self.add_tournament_controller = AddTournamentController()
                self.tournament = self.add_tournament_controller.add_new_tournament()
            elif option_selected == MainMenuOptions.LOAD_TOURNAMENT:
                if not self.load_tournament_controller:
                    self.load_tournament_controller = LoadTournamentController()
                tournaments = self.tournaments
                action_menu_controller = ActionMenuController()
                action_menu_controller.start_loop()
            elif option_selected == MainMenuOptions.SHOW_REPORTS:
                if not self.show_report_controller:
                    self.show_report_controller = ReportsMenuController(self.player_manager)
                self.show_report_controller.start_loop()
