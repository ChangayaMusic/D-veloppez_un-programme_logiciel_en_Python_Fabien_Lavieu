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
    def __init__(self, tournament):
        self.view = TournamentActionsMenu()
        self.tournament = tournament
        self.player_manager = PlayerManager()

    def start_loop(self):
        option_selected = ActionMenuOptions.UNASSIGNED
        while option_selected != ActionMenuOptions.EXIT:
            option_selected = int(self.view.select_action())
            if option_selected == ActionMenuOptions.ADD_PLAYER:
                players = self.player_manager.load_players_from_json()
                self.view.show_players(players)
                players_to_add = self.view.get_players_ids(players_to_add=[])
                players_founds = []
                for player_id in players_to_add:
                    player = self.player_manager.find_player_by_identification(player_id, players)
                    if player:
                        players_founds.append(player)
                self.tournament.players = players_founds    
            elif option_selected == ActionMenuOptions.EXIT:
                pass