import datetime
from player import Player   

class Tournament:
    def __init__(self, tournament_name, place, nb_rounds=4, players = [],
                description = '', round_list = [], **kwargs):
        
        self.tournament_name = tournament_name
        self.place = place
        self.nb_rounds = nb_rounds
        self.players = players
        self.star_time = start_time
        self.end_time = end_time
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
    
tournament1 = Tournament('chess kings', 'Orleans')




