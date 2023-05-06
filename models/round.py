import datetime
import random
from match import Match
from tournament import Tournament
from player import Player


class Round:
    
    def __init__(self,name, matches, round_date_hour_start, round_date_hour_end, round_players = []):
        
        self.name = name
        self.matches= matches
        self.round_date_hour_start = round_date_hour_start
        self.round_date_hour_end = round_date_hour_end 
        self.round_players = round_players
    
        
    @property
    def start_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def end_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
        
        
    def first_round_mix(self, round_player_list):
        Tournament.players = random.shuffle(Tournament.players)
    
    def player_by_points_mix(self, round_player_list):
        Tournament.players = Tournament.players.sort(key=lambda x: Player.points)
        
    def generate_match(self):
        for i in range(0, len(players)-1, 2):
            matches.append((players[i], players[i+1]))

   
       
       
 
        


        
        
    
    
    
    
        
    
    
    
    
    
        
    
    
    
    