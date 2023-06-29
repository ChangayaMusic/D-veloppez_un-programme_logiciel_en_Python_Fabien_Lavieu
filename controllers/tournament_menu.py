from enum import IntEnum
from views.menus import TournamentActionsMenu
from models.player import PlayerManager
from models.round import Round, RoundManager
from models.tournament import Tournament, TournamentManager
from views.view_tournament import LoadTournamentView


class ActionMenuOptions(IntEnum):
    UNASSIGNED = -1
    ADD_PLAYER = 0
    START_TOURNAMENT = 1
    END_TOURNAMENT = 2
    EXIT = 3


class ActionMenuController:
    def __init__(self, ):
        self.view = TournamentActionsMenu()
        self.tournament = None
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.round_manager = RoundManager()
        self.tournaments = self.tournament_manager.load_tournaments_from_file()
        self.tournament_name = None

    def start_loop(self):
        LoadTournamentView.show_tournaments_name_date(self.tournaments)
        self.tournament_name = LoadTournamentView.ask_for_tournament(
            self.tournaments)
        tournament = self.tournament_manager.load_tournament_by_name(
            self.tournament_name)

        if tournament:
            self.tournament = tournament
            LoadTournamentView.tournament_loaded(self)
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
                    players_found = self.player_manager.find_player_by_identification(
                        player_id)
                    if players_found:
                        for player in players_found:
                            self.tournament_manager.add_player_to_tournament(
                                self.tournament_name, player)
                self.tournament_manager.update_tournaments_file()
                self.view.tournaments_updated()
                print(self.tournament.players)
                self.start_loop()

            if option_selected == ActionMenuOptions.START_TOURNAMENT:
                self.tournament.start_time = Tournament.get_current_time()
                self.round_manager.create_rounds(self.tournament)

                for round in self.tournament.rounds:
                    if "1" in round.name:
                        round.get_first_round_players(self.tournament)
                        print(round.matches)
                        for match in round.matches:
                            player1 = match[0]
                            print(player1)
                            player2 = match[1]
                            print(player2)
                            result = self.view.get_match_winner(
                                player1, player2)
                            if result not in [1, 2, 3]:
                                self.view.wrong-result()
                            else:
                                self.round_manager.set_score(
                                    result, player1, player2)

                        tournament.players = self.round_manager.sort_by_points(
                            self.tournament.players)
                        for player in tournament.players:
                            print(
                                f"Player: {player['first_name']} {player['last_name']}, Points: {player['points']}, Rank: {player['rank']}")
                    else:

                        print(round.name)
                        players = tournament.players
                        self.matches = round.matchmaking_by_points(players)
                        print(round.matches)
                        for match in self.matches:
                            player1 = match[0]
                            print(player1)
                            player2 = match[1]
                            print(player2)
                            result = self.view.get_match_winner(
                                player1, player2)
                            self.round_manager.set_score(
                                result, player1, player2)
                        tournament.players = self.round_manager.sort_by_points(
                            self.tournament.players)

                self.round_manager.update_tournaments_rounds_file(tournament)
                self.tournament_manager.update_players_points()
            if option_selected == ActionMenuOptions.END_TOURNAMENT:
                tournament.end_time = Tournament.end_time
                 
            elif option_selected == ActionMenuOptions.EXIT:
                pass
