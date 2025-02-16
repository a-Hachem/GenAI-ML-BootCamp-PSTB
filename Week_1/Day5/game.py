import random



class Game():
    def __init__(self):
        self.choices =["r", "p", "s"] 

    def get_user_item(self):
        while True:
            user_item = input("Enter a choice among r , p or s : " ).lower()
            if user_item in self.choices:
                return user_item
            else:
                  print("Invalid choice. Please try again.")
                 
    
    def get_computer_item(self):
        comp_item= random.choice(self.choices)
        return comp_item
    
    def get_game_result(self, user_item, comp_item):
            if user_item == "r" and comp_item == "p":
                return f"You lost!"
            elif (user_item == "r" and comp_item == "s") or \
                 (user_item == "p" and comp_item == "r") or \
                 (user_item == "s" and comp_item == "p"):
                 return "You won!"       
            else:
                 return "You drew!"
                 
              
    def play(self):
        """
       Plays a single round of Rock-Paper-Scissors.
    - Gets the user’s choice.
    - Gets the computer’s choice.
    - Determines the result of the game.
    - Displays the result.
    - Returns the result as a string: "win", "loss", or "draw".
       
       """
        user_item = self.get_user_item()  #Récupère le choix de l'utilisateur
        comp_item = self.get_computer_item()  # Récupère le choix de l'ordinateur
        result = self.get_game_result(user_item, comp_item)  # Détermine le gagnant

        #Affiche les choix et le résultat
        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {comp_item}")
        print(result)

        #Retourne le résultat sous forme de string utilisable
        if result == "You won!":
          return "win"
        elif result == "You lost!":
          return "loss"
        else:
          return "draw"

    
         
               
            