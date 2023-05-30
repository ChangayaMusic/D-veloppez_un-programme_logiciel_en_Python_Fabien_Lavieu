from enum import IntEnum
from views.menu import MainMenuView
from models.player import PlayerManager, Player
from models.tournament import Tournament
from controllers.menu_player import AddPlayerController
from controllers.menu_tournament import AddTournamentController, LoadTournamentController
from controllers.create_round import CreateRoundController
from controllers.report_menu import ReportsMenuController
from controllers.action_menu import ActionMenuController
from views.view_tournament import LoadTournamentView


class MainMenuOptions(IntEnum):
    UNASSIGNED = -1
    NEW_PLAYER = 0
    NEW_TOURNAMENT = 1
    NEW_ROUND = 2
    LOAD_TOURNAMENT = 3
    SHOW_REPORTS = 4
    EXIT = 5


class MainMenuController:
    def __init__(self):
        self.player_manager = PlayerManager()
        self.add_player_controller = None
        self.view = MainMenuView()
        self.view.display_welcome()
        self.add_tournament_controller = None
        self.add_round_controller = None
        self.load_tournament_controller = None
        self.show_report_controller = None
        self.tournament = None

    def start_loop(self):
        option_selected = MainMenuOptions.UNASSIGNED
        while option_selected != MainMenuOptions.EXIT:
            option_selected = int(self.view.select_option())
            if option_selected == MainMenuOptions.NEW_PLAYER:
                if not self.add_player_controller:
                    self.add_player_controller = AddPlayerController(self.player_manager)
                player = self.add_player_controller.add_new_player()
                
            elif option_selected == MainMenuOptions.NEW_TOURNAMENT:
                if not self.add_tournament_controller:
                    self.add_tournament_controller = AddTournamentController()
                self.tournament = self.add_tournament_controller.add_new_tournament()
            elif option_selected == MainMenuOptions.LOAD_TOURNAMENT:
                if not self.load_tournament_controller:
                    self.load_tournament_controller = LoadTournamentController()
                    ActionMenuController.start_loop(self)
            elif option_selected == MainMenuOptions.NEW_ROUND:
                if not self.add_round_controller:
                    self.add_round_controller = CreateRoundController()
                self.add_round_controller.new_round(self.tournament)
            elif option_selected == MainMenuOptions.SHOW_REPORTS:
                if not self.show_report_controller:
                    self.show_report_controller = ReportsMenuController(self.player_manager)
                self.show_report_controller.start_loop()
