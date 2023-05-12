# from views.viewplayer import ViewPlayer

class MainMenuView:
    def display_welcome(self):
        print("Welcome in the chess tournament manager !")

    def select_option(self):
        return input(
            "Please choose an option to continue:\n"
            "0: Create a new player\n"
            "1: Create a new tournament\n"
            "2: Continue an existing tournament\n"
            "3: Show reports\n"
            "4: Exit\n"
            "Your choice ? "
        )

