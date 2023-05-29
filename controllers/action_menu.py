from enum import IntEnum
from views.menu import TournamentActionsMenu
from models.player import PlayerManager


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
                players = self.player_manager.load_players_from_json()
                self.view.show_players(players)

                players_to_add = self.view.get_players_ids(players_to_add=[])
                print(players_to_add)
                
                
            elif option_selected == ActionMenuOptions.EXIT:
                pass

    @staticmethod
    def add_players_by_name(players, players_to_add, tournament):
        for player in players:
            if player.name in players_to_add:
                tournament.players.append(player)
        return players_to_add
