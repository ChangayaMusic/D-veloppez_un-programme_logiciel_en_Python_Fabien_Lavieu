import datetime
import json
import random

class Round:
    def __init__(self, name="", matches=[], start_time=None, end_time=None):
        self.name = name
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time

    def start(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def end(self):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def get_first_round_players(self, tournament):
        players = tournament.players
        random.shuffle(players)
        pairs = zip(*[iter(players)] * 2)
        for pair in pairs:
            self.matches.append(pair)

       
class RoundEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Round):
            round_dict = {
                'name': obj.name,
                'matches': obj.matches,
                'start_time': obj.start_time,
                'end_time': obj.end_time
            }
            return round_dict
        return super().default(obj)

def round_decoder(obj):
    if 'name' in obj:
        return Round(
            name=obj['name'],
            matches=obj['matches'],
            start_time=obj['start_time'],
            end_time=obj['end_time']
        )
    return obj

class RoundManager:
    def __init__(self):
        self.rounds = []
        self.round_instance = 1

    def create_rounds(self, tournament):
        for _ in range(tournament.nb_rounds):
            round_name = f"round{self.round_instance}"
            round_instance = Round(name=round_name)
            round_instance.start()
            tournament.rounds.append(round_instance)
            
            self.round_instance += 1

    
    def update_tournaments_rounds_file(self, tournament):
        with open('tournaments.json', 'r') as file:
            data = json.load(file)

        tournament_list = data
        for t in tournament_list:
            if t['tournament_name'] == tournament.tournament_name:
                # Update the rounds of the tournament
                t['rounds'] = [round_obj for round_obj in tournament.rounds]
                break

        with open('tournaments.json', 'w') as file:
            json.dump(data, file, indent=4, cls=RoundEncoder)

    def set_winner(self, result, match):
        if result == 1:
            match.player1.points += 1  
            match.player2.points += 0  
            match.player1.opponents.append(match.player2)  
            return match.player1
        elif result == 2:
            match.player1.points += 0  
            match.player2.points += 1 
            match.player2.opponents.append(match.player1)  
            return match.player2
        elif result == 3:
            match.player1.points += 0.5  
            match.player2.points += 0.5  
            match.player1.opponents.append(match.player2) 
            match.player2.opponents.append(match.player1) 
            return None  
        else:
            print("Invalid input. Please choose 1, 2, or 3.")   
            
    def sort_by_points(self, players):
        return sorted(players, key=lambda player: player.points, reverse=True)                
