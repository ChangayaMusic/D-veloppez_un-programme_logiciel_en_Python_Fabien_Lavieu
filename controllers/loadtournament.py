from views.viewtournament import LoadTournamentView
from models.round import Round
from models.tournament import Tournament
import json
class LoadTournamentController:
    def __init__(self):
        self.view = LoadTournamentView()

    def load_tournaments_from_file(self):
        with open('tournaments.json', 'r') as file:
            tournaments = json.load(file)
        return tournaments

    def load_tournament_by_name(self, tournament_name):
        tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament['tournament_name'] == tournament_name:
                self.view.tournament_loaded(tournament)
                return tournament
        self.view.tournament_is_not_in_db()

    