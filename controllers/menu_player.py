from views.viewplayer import AddPlayerView
from models.player import Player
from datetime import datetime

class AddPlayerController:
    def __init__(self):
        self.view = AddPlayerView()
    
    def validate_identification(self, identification):
        result = identification and len(identification) == 7
        if not result:
            self.view.display_identification_error()
        return result

    def add_new_player(self):
        identification = None
        first_name = None
        last_name = None
        while not first_name:
            first_name = self.view.input_first_name()
        while not last_name:
            last_name = self.view.input_last_name()
        while not self.validate_identification(identification):
            identification = self.view.input_identification()
        player = Player(last_name=last_name, surname=first_name, birth_date=datetime.now(), identification=identification)
        self.view.print_player_added(player)
        return player