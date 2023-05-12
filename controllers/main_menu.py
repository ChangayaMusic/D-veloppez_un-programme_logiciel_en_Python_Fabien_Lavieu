from models.tournament import Tournament
from controllers.menu_player import AddPlayerController
from controllers.menu_tournament

from views.menu import MainMenuView
from enum import IntEnum

class MainMenuOptions(IntEnum):
    UNASSIGNED = -1
    NEW_PLAYER = 0
    NEW_TOURNAMENT = 1
    LOAD_TOURNAMENT = 2
    SHOW_REPORTS = 3
    EXIT = 4


class MainMenuController:
    def __init__(self) -> None:
        self.tournament = Tournament("Test Tournament", "Paris")
        self.add_player_controller = None
        self.view = MainMenuView()
        self.view.display_welcome()

    def start_loop(self):
        option_selected = MainMenuOptions.UNASSIGNED
        while option_selected != MainMenuOptions.EXIT:
            option_selected = int(self.view.select_option())
            if option_selected == MainMenuOptions.NEW_PLAYER:
                if not self.add_player_controller:
                    self.add_player_controller = AddPlayerController()
                self.tournament.players.append(self.add_player_controller.add_new_player())
            if option_selected == MainMenuOptions.NEW_TOURNAMENT:
                if not self.add_tournament_controller:
                    self.add_tournament_controller = AddTournamentController
                
                    