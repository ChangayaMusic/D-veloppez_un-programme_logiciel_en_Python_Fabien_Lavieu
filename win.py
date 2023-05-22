<<<<<<< HEAD:win.py
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
=======


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
>>>>>>> 65e8627d2701bdb0513e83d0c76cf664d7b1c328:views/win.py
    print(match.match_player_1_score, match.match_player_2_score, match.is_equality)