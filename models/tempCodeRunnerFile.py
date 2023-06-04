    tournaments = self.load_tournaments_from_file()
        for tournament in tournaments:
            if tournament.tournament_name == tournament_name:
                return tournament
        return None
    