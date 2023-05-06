from match import Match

class Player:
   
    
    def __init__(self, last_name , surname , birth_date, identification,
                points=0, opponents = [], tournament_score = 0, rank=0):
        self.last_name = last_name
        self.surname = surname
        self.birth_date = birth_date
        self.identification = identification
        self.points = points
        self.rank = rank
        self.opponents = opponents
        self.tournament_score = tournament_score
    
doudou = Player('Doudou', 'Ophélia', '1995-05','45')

boubou = Player('Boubou', 'Alikea','2007-03','nahsheitan1')

rico = Player('Rico', 'El famoso','1972-012','37')

changaya = Player('Changaya', 'fabien','1989-09','93')

    
