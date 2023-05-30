from enum import IntEnum
from views.menu import TournamentActionsMenu, MainMenuView
from models.player import PlayerManager
from models.tournament import Tournament
from views.view_tournament import LoadTournamentView
from controllers.menu_tournament import LoadTournamentController


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
        self.load_tournament_controller = LoadTournamentController()

    def start_loop(self):
        tournaments = self.load_tournament_controller.load_tournaments_from_file()
        LoadTournamentView.show_tournaments_name_date(tournaments)
        tournament_name = LoadTournamentView.ask_for_tournament(tournaments)
        loaded_data = self.load_tournament_controller.load_tournament_by_name(tournaments, tournament_name)

        if loaded_data:
            self.tournament = loaded_data
            print('_data loaded successfully')
        else:
            self.view.data_error()
            return

        option_selected = ActionMenuOptions.UNASSIGNED
        while option_selected != ActionMenuOptions.EXIT:
            self.view = TournamentActionsMenu()
            option_selected = int(self.view.select_action())
            if option_selected == ActionMenuOptions.ADD_PLAYER:
                players = self.player_manager.load_players_from_json()
                self.view.show_players(players)
                players_to_add = self.view.get_players_ids(players_to_add=[])
                found_players =[]
                for player_id in players_to_add:
                    players_found = self.player_manager.find_player_by_identification(player_id, players,found_players)
                    print(found_players)
                    if found_players:
                        for player in found_players:
                            self.tournament.players.append(player)
                Tournament.update_tournament(tournaments, self.tournament)
                print(self.tournament.__dict__)
                
                Tournament.save_tournaments_to_file(tournaments)
                
                print("YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            elif option_selected == ActionMenuOptions.EXIT:
                pass
