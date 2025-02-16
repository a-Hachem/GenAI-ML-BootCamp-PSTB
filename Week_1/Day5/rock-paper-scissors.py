from game import Game  # Importe la classe Game depuis le module game

def get_user_menu_choice():
    """
    Affiche un menu et demande à l'utilisateur de faire un choix.
    Retourne le choix de l'utilisateur (1, 2, ou 3).
    """
    print("\n--- Menu ---")
    print("g. Play a new game")
    print("c. Show scores")
    print("x. Quit")
    choice = input("Enter your choice (g, c, or x ): ").strip()
    return choice

def print_results(results):
    """
    Affiche les résultats des parties jouées.
    """
    print("\n--- Game Results ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    """
    Fonction principale du programme.
    """
    results = {"win": 0, "loss": 0, "draw": 0}  # Dictionnaire pour stocker les résultats

    while True:
        choice = get_user_menu_choice() # If the game enter 1 or 2 or 3, the gamer input is stored

        if choice == "g":  
             new_game = Game()  # Crée un nouvel objet Game
             result = new_game.play()  # Joue une partie et récupère le résultat
             results[result] += 1  # Met à jour les résultats

        elif choice == "c":  # Afficher les scores
            print_results(results)

        elif choice == "x":  # Quitter
            print_results(results)
            print("Goodbye!")
            break

        else:  # Choix invalide
            print("Invalid choice. Please enter g, c, or x.")

# Lance le programme
if __name__ == "__main__":
    main()