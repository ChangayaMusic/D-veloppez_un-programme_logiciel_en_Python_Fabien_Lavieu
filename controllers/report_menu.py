import json
from views.menus import ReportMenuView
from enum import IntEnum
from controllers.add_tournament import LoadTournamentController
from models.player import PlayerManager
from views.view_tournament import LoadTournamentView
from models.tournament import TournamentManager, Tournament
from views.view_tournament import AddTournamentView
class ReportsMenuOptions(IntEnum):
    UNASSIGNED = -1
    ALL_PLAYERS = 0
    TOURNAMENT_LIST = 1
    TOURNAMENT_DATE_NAME = 2
    TOURNAMENT_PLAYERS = 3
    TOURNAMENT_ROUNDS_MATCHES = 4
    EXIT = 5

class ReportsMenuController:
    def __init__(self, player_manager):
        self.load_tournament_controller = LoadTournamentController()
        self.view = ReportMenuView()
        self.player_manager = player_manager
        self.tournament_list = None
        self.tournament_date_name = None
        self.tournament_players = None
        self.rounds_matches = None
        self.tournament_manager = TournamentManager

    def start_loop(self):
        
        option_selected = ReportsMenuOptions.UNASSIGNED
        while option_selected != ReportsMenuOptions.EXIT:
            option_selected = int(self.view.select_report())

            if option_selected == ReportsMenuOptions.ALL_PLAYERS:
                print("all players by name")
                players = PlayerManager.load_players_from_json(self)
                self.view.display_all_players(players)

            if option_selected == ReportsMenuOptions.TOURNAMENT_LIST:
                tournaments = self.tournament_manager.load_tournaments_from_file(self)
                self.view.show_tournaments_list(tournaments)
                    
                        

            if option_selected == ReportsMenuOptions.TOURNAMENT_DATE_NAME:
                tournaments = self.tournament_manager.load_tournaments_from_file(self)
                
                tournament_name = AddTournamentView.input_tournament_name(self)
                print(tournament_name)
                for tournament in tournaments:
                    if tournament.tournament_name == tournament_name:
                        ReportMenuView.show_tournaments(tournament)
                        
                        
            if option_selected == ReportsMenuOptions.TOURNAMENT_PLAYERS:
                ReportMenuView.display_tournament_players()
                players_to_sort = []
                tournaments = self.tournament_manager.load_tournaments_from_file(self)
                self.view.show_tournaments_list(tournaments)
                tournament_name = AddTournamentView.input_tournament_name(self)
                for tournament in tournaments:
                    if tournament.tournament_name == tournament_name:
                        self.tournament = tournament
                        for player in tournament.players:
                            players_to_sort.append(player)
                        players = sorted(players_to_sort, key=lambda player: player["last_name"])
                        for player in players:
                            ReportMenuView.player_infos(player)


            if option_selected == ReportsMenuOptions.TOURNAMENT_ROUNDS_MATCHES:
                with open('tournaments.json') as file:
                    data = json.load(file)
                    tournament_name = AddTournamentView.input_tournament_name(self)
                    tournament_found = False

                    for tournament in data:
                        if tournament_name == tournament['tournament_name']:
                            print("Tournament:", tournament['tournament_name'])
                            tournament_found = True

                            # Iterate over the rounds in the tournament
                            for round_data in tournament["rounds"]:
                                round_name = round_data["name"]
                                print("Round:", round_name)

                                # Iterate over the matches in the round
                                for match in round_data["matches"]:
                                    print("Match:")
                                    for p in match:
                                        print(p['identification'], p['first_name'], p['last_name'])



                    if not tournament_found:
                        print("No tournament found")


