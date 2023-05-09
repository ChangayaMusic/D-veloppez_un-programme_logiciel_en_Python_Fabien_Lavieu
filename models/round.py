import datetime
import random
from tournament import Tournament
from player import Player
import itertools
# a mettre dans tournament ?

class Round:
    def __init__(self, name, matches=[], start_time=None, end_time=None,score={}, players=[], rounds = [], **kwargs):
        self.name = name
        self.matches = []
        self.start_time = start_time
        self.end_time = end_time
        self.score = score
        self.players = players
        
    def start(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def end(self,rounds):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%Y-%m-%d %H:%M:%S")
        rounds.append(Round(self))
        
        
    def randomize_players(self,players):
        self.players = Tournament.players = random.shuffle(Tournament.players)
        
    def sort_by_points(self, players):
        self.players = Tournament.players.sort(key=lambda x: x.points, reverse=True)
    
    def get_eligible_opponents(self, player_list):
        eligible_opponents = []
        for player in player_list:
            if player.points == self.points and player.identification not in self.opponents:
                eligible_opponents.append(player)
        return eligible_opponents
    
    def get_random_opponent(self, eligible_opponents):
        if not eligible_opponents:
            return None
        return random.choice(eligible_opponents)
        
    def generate_pairs(players,matches):
    
        used_players = []
        
        for player in players:
            if player.identification in used_players:
                continue
            eligible_opponents = player.get_eligible_opponents(players)
            random_opponent = player.get_random_opponent(eligible_opponents)
            if random_opponent:
                matches.append((player, random_opponent))
                
    
        
            
    
        
                

        

        
    
tournament1 = Tournament('chess kings', 'Orleans')

doudou = Player('Doudou', 'Ophélia', '1995-05','45')

boubou = Player('Boubou', 'Alikea','2007-03','nahsheitan1')

rico = Player('Rico', 'El famoso','1972-012','37')

changaya = Player('Changaya', 'fabien','1989-09','93')

tournament1.players =[doudou, changaya, boubou, rico]

tournament1.description = 'First try'

round1 = Round('round1')

round1.start()

print(tournament1.players)

tournament1.randomize_players()

print(tournament1.players)



        
        
    
    
    
    
        
    
    
    
    
    
        
    
    
    
    