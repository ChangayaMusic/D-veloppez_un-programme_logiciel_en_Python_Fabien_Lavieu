from enum import IntEnum
from views.menu import TournamentActionsMenu
from models.player import PlayerManager
from controllers.menu_tournament import TournamentsActions



class ActionMenuOptions(IntEnum):
    UNASSIGNED = -1
    ADD_PLAYER = 0
    NEW_TOURNAMENT = 1
    NEW_ROUND = 2
    LOAD_TOURNAMENT = 3
    SHOW_REPORTS = 4
    EXIT = 5
    
class ActionMenuController:
    def __init__(self):
        self.view = TournamentActionsMenu()
        self.player_manager = PlayerManager()

    def start_loop(self, tournament):
        option_selected = ActionMenuOptions.UNASSIGNED
        while option_selected != ActionMenuOptions.EXIT:
            option_selected = int(self.view.select_action())
            if option_selected == ActionMenuOptions.ADD_PLAYER:
                players=PlayerManager.load_players_from_json()
                TournamentsActions.add_player_to_tournament(players, tournament)
            elif option_selected == ActionMenuOptions.EXIT:
                pass
                    