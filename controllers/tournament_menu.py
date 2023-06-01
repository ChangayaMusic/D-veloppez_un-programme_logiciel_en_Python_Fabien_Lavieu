from enum import IntEnum
from views.menus import TournamentActionsMenu
from models.player import PlayerManager
from models.tournament import Tournament, TournamentManager
from views.view_tournament import LoadTournamentView
from controllers.add_tournament import LoadTournamentController


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
        self.tournament = None
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.tournaments = self.tournament_manager.load_tournaments_from_file()
        self.tournament_name = LoadTournamentView.ask_for_tournament(self.tournaments)
        self.tournament =self.tournament.load_tournament_by_name(self.tournament_name)

    def start_loop(self,tournaments):
        
        LoadTournamentView.show_tournaments_name_date(tournaments)
        
        print(self.tournaments)

        option_selected = ActionMenuOptions.UNASSIGNED
        while option_selected != ActionMenuOptions.EXIT:
            self.view = TournamentActionsMenu()
            option_selected = int(self.view.select_action())
            if option_selected == ActionMenuOptions.ADD_PLAYER:
                self.view.show_players(self.player_manager.players)
                players_to_add = self.view.get_players_ids(players_to_add=[])
                for player_id in players_to_add:
                    players_found = self.player_manager.find_player_by_identification(player_id)
                    print(players_found)
                    if players_found:
                        for player in players_found:
                            self.tournament.players.append(player)
                self.tournament_manager.update_tournament(self.tournament)
                
                
                print("YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            elif option_selected == ActionMenuOptions.EXIT:
                pass
