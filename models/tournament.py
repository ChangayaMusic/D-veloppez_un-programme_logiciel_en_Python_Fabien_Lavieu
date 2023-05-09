import datetime
import random
# from player import Player
# from round import Round

class Tournament:
    def __init__(self, tournament_name, place, nb_rounds=4, players = [],
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


# if __name__ == '__main__':
#     tournament1 = Tournament('chess kings', 'Orleans')

#     doudou = Player('Doudou', 'Ophélia', '1995-05', '45')
#     boubou = Player('Boubou', 'Alikea', '2007-03', 'nahsheitan1')
#     rico = Player('Rico', 'El famoso', '1972-012','37')
#     changaya = Player('Changaya', 'Fabien', '1989-09', '93')

#     tournament1.players = [doudou, changaya, boubou, rico]
#     tournament1.description = 'First try'

#     round1 = Round('round1')
#     round1.start()
    
#     print(tournament1.players)
#     tournament1.randomize_players()
#     print(tournament1.players)
