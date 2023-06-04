import datetime
import json
import random

class Round:
    def __init__(self, round_instance=None, name="", matches=[], start_time=None, end_time=None, tournament=None):
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

class RoundEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Round):
            round_dict = {
                'name': obj.name,
                'round_instance': obj.round_instance,
                'matches': obj.matches,
                'start_time': obj.start_time,
                'end_time': obj.end_time,
                'tournament': obj.tournament,
            }
            return round_dict
        return super().default(obj)

class RoundManager:
    def __init__(self):
        self.rounds = []
        self.round_instance = 1

    def create_rounds(self, tournament):
        for _ in range(tournament.nb_rounds):
            round_name = f"round{self.round_instance}"
            round_instance = Round(name=round_name, tournament=tournament)
            round_instance.start()
            tournament.round_list.append(round_instance)
            self.rounds.append(round_instance)
            self.round_instance += 1
            self.tournament = tournament.tournament_name

    def first_round_player(self, players):
        random.shuffle(players)
        pairs = zip(*[iter(players)] * 2)
        return list(pairs)
    
    def update_tournaments_rounds_file(self,tournament):
        with open('tournaments.json', 'r') as file:
            data = json.load(file)
            
            tournament_list = data
            for t in tournament_list:
                if t['tournament_name'] == tournament.tournament_name:
                    # Update the round_list of the tournament
                    t['round_list'] = [round_obj for round_obj in tournament.round_list]
                    break
            
        with open('tournaments.json', 'w') as file:
            json.dump(data, file, indent=4, cls=RoundEncoder)


            
