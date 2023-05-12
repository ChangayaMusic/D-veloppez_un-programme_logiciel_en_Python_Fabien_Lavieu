from views.viewplayer import AddPlayerView
from models.player import Player
from datetime import datetime
import re

class AddPlayerController:
    def __init__(self):
        self.view = AddPlayerView()
    
    def validate_identification(self, identification):
        pattern = r'^[a-zA-Z]{2}\d{4}$'
        if re.match(pattern, identification):
            return identification
        else:
            self.view.display_identification_error()
            return None  # return None if identification is invalid

    def add_new_player(self):
        identification = None
        first_name = None
        last_name = None
        birth_date = None
        while not first_name:
            first_name = self.view.input_first_name()
        while not last_name:
            last_name = self.view.input_last_name()
        while not identification:
            identification = self.view.input_identification()
            identification = self.validate_identification(identification)  # validate identification
        
        while not birth_date:
            try:
                birth_date = self.view.input_birth_date()
                birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
            except ValueError:
                self.view.display_birth_date_error()
                
        player = Player(last_name=last_name, first_name=first_name, birth_date=birth_date, identification=identification)
        return player
        Player.check_if_in_db(player)
        if result:
            self.view.already_in_db(player)
        else:
            Player.add_player_to_db(player)
            self.view.bd_validation

        self.view.print_player_added(player)
