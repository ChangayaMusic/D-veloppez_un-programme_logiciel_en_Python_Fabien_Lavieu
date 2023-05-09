import datetime
import random
from tournament import Tournament
from player import Player
# a mettre dans tournament ?
class Round:
    def __init__(self, name, matches={}, start_time=None, end_time=None,score={}):
        self.name = name
        self.matches = matches or []
        self.start_time = start_time
        self.end_time = end_time
        self.score = score
        
    def start(self):
        now = datetime.datetime.now()
        self.start_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def end(self):
        now = datetime.datetime.now()
        self.end_time = now.strftime("%Y-%m-%d %H:%M:%S")
        

        
    
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



        
        
    
    
    
    
        
    
    
    
    
    
        
    
    
    
    