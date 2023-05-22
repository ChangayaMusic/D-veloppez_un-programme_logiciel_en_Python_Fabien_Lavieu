from views.view_round import RoundView
from models.round import Round

class CreateRoundController:
    def __init__(self):
        self.view = RoundView()
        
    def new_round(self, tournament):
        round_obj = Round()
        round_obj.create_first_round(tournament)
