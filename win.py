from models.match import Match

if __name__ == "__main__":
    # We are in controller Match
    match = Match()
    print(match.match_player_1_score, match.match_player_2_score, match.is_equality)
    # MatchMenuView.Display_input_result
    result = input(
        "Which is the result of the match ?\n"
        "0: Player 1 wins\n"
        "1: Player 2 wins\n"
        "2: Equality\n"
    )
    # Call Match model modification
    match.set_result(int(result))
    print(match.match_player_1_score, match.match_player_2_score, match.is_equality)