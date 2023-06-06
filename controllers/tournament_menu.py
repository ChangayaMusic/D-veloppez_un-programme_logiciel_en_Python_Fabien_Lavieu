from enum import IntEnum
from views.menus import TournamentActionsMenu
from models.player import PlayerManager
from models.round   import Round, RoundManager
from models.tournament import Tournament, TournamentManager
from views.view_tournament import LoadTournamentView


class ActionMenuOptions(IntEnum):
    UNASSIGNED = -1
    ADD_PLAYER = 0
    START_TOURNAMENT = 1
    END_TOURNAMENT = 2
    EXIT = 3


class ActionMenuController:
    def __init__(self):
        self.view = TournamentActionsMenu()
        self.tournament = None
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.round_manager = RoundManager()
        self.tournaments = self.tournament_manager.load_tournaments_from_file()
        self.tournament_name = None
        

    def start_loop(self):
        LoadTournamentView.show_tournaments_name_date(self.tournaments)
        self.tournament_name = LoadTournamentView.ask_for_tournament(self.tournaments)
        tournament = self.tournament_manager.load_tournament_by_name(self.tournament_name)

        if tournament:
            self.tournament = tournament
            print('Data loaded successfully')
            print(self.tournament)
        else:
            self.view.data_error()
            return

        option_selected = ActionMenuOptions.UNASSIGNED
        while option_selected != ActionMenuOptions.EXIT:
            self.view = TournamentActionsMenu()
            option_selected = int(self.view.select_action())
            if option_selected == ActionMenuOptions.ADD_PLAYER:
                self.view.show_players(self.player_manager.players)
                players_to_add = self.view.get_players_ids(players_to_add=[])
                for player_id in players_to_add:
                    players_found = self.player_manager.find_player_by_identification(player_id)
                    if players_found:
                        for player in players_found:
                           self.tournament_manager.add_player_to_tournament(self.tournament_name, player)
                self.tournament_manager.update_tournaments_file()
                self.view.tournaments_updated()
                print(self.tournament.players)
            if option_selected == ActionMenuOptions.START_TOURNAMENT:
                self.tournament.start_time = Tournament.get_current_time()
                self.round_manager.create_rounds(self.tournament)
                
                self.round_manager.update_tournaments_rounds_file(tournament)
                print(self.tournament.rounds)
                for round in self.tournament.rounds:
                    print(round.name)
                # If first round, create first round matches
                # Then , create matches with matchmaking (more or less naive)
                
            elif option_selected == ActionMenuOptions.EXIT:
                pass