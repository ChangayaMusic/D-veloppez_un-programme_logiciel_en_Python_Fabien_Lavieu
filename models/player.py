from tinydb import TinyDB, Query
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
    
    def __repr__(self) -> str:
        return f"{ self.last_name } { self.surname } - { self.identification }"
    
    def check_if_in_db(self, player):
        db = TinyDB('players.json')
        PlayerTable = Query()
        result = db.search(PlayerTable.identification == player.identification)
        return result
    
    def add_player_to_db(self, player):
        
        
        db = TinyDB('players.json')
        db.insert(player.__dict__)
            
       

    
        

    
