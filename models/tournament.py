import datetime
import random
from player import Player   

class Tournament:
    def __init__(self, tournament_name, place, nb_rounds=4, players = {},
                description = '', round_list = [], **kwargs):
        
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = players
        self.description = description
        self.round_list = round_list
    
   
    @property
    def start_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
    
    def randomize_players(self,players):
        players = random.shuffle(players)
        
        
    def sort_by_points(self, players):
        players.sort(key=lambda x: x.points, reverse=True)
        
    
        
    




