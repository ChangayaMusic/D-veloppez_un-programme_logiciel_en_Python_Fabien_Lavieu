import random
from tournament import Tournament


class Match:
  
 
    
def __init__(self,player_1, player_2, match):
          
        #match sould be a tulpe
    @property
    def is_equality(self):
        return self.match_player_1_score != 0 and self.match_player_2_score != 0 \
               and self.match_player_1_score == self.match_player_2_score

    def set_result(self, result):
        if result == ResultMatch.PLAYER_1_WINS:
            self.match_player_1_score = 1
        elif result == ResultMatch.PLAYER_2_WINS:
            self.match_player_2_score = 1
        elif result == ResultMatch.EQUALITY:
            self.match_player_1_score = self.match_player_2_score = 0.5
        else:
            raise ValueError("Unknown result match value")
    
    
 



