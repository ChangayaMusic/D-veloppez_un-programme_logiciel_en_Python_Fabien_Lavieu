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

# class Menu:
#     def mainnmenu():    
#         while True:
#             print("Please choose an option:")
#             print("1 - Create a new player")
#             print("2 - Create a new tournament")
#             print("3 - Continue an existing tournament")
#             print("4 - Show reports")
#             print("5 - Exit")

#             choice = input("Enter your choice (1-5): ")

#             if choice == '1':
#                 print("You chose option 1")
#                 ViewPlayer.create_player()
#             elif choice == '2':
#                 print("You chose option 2")
#             elif choice == '3':
#                 print("You chose option 3")
#             elif choice == '4':
#                 print("You chose option 4")
#             elif choice == '5':
#                 print("Exiting program...")
#                 break
#             else:
#                 print("Invalid choice. Please enter a number between 1 and 5.")