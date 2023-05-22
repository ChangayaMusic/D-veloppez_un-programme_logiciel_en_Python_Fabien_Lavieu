import datetime
from models.tournament import Tournament
import random

class Round:
    def __init__(self, round_instance=None, name="", matches=[], start_time=None, end_time=None,tournament=None):
        self.name = name
        self.round_instance = round_instance
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time
        self.tournament = tournament

    def start(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def end(self):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def create_first_round(self, tournament):
        round_players = tournament.players.copy()
        if self.round_instance is None:
            self.round_instance = 1
            
            random.shuffle(round_players)
            pairs = zip(*[iter(round_players)] * 2)
            for pair in pairs:
                self.matches.append(pair)
            self.name = f"round {self.round_instance}"
            Tournament.round_list.append(self)
            self.round_instance += 1
            self.start()
        else:
            self.create_round()

    def create_round(self):
        sorted_players = sorted(Tournament.players, key=lambda player: player.points, reverse=True)
        grouped_players = []
        current_group = [sorted_players[0]]
        for i in range(1, len(sorted_players)):
            if sorted_players[i].points == sorted_players[i - 1].points:
                current_group.append(sorted_players[i])
            else:
                grouped_players.append(current_group)
                current_group = [sorted_players[i]]
        grouped_players.append(current_group)

        for group in grouped_players:
            if len(group) > 1:
                random.shuffle(group)

        for i in range(0, len(sorted_players), 2):
            pair = (sorted_players[i], sorted_players[i + 1]) if i + 1 < len(sorted_players) else (sorted_players[i], None)
            self.matches.append(pair)

        self.name = f"round {self.round_instance}"
        Tournament.round_list.append(self)
        self.round_instance += 1
        self.start()
