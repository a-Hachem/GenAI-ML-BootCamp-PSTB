### Modules

1 fichier pour l'affichage du menu (rock-paper-scissors.py)
1 fichier pour la logique du jeu (game.py)

### PAGE game.py

class Game

#### function get_user_item(self)

1. demande a l'utilisateur soit de rentrer "r" pour rock, "p" paper, "s" scissors
2. verifie que la reponse est r, soit p, soit s 
    -> tant que sa reponse n'est pas r, soit p, soit s : ... or ... or ...
        -> notion de condition True ou False
    -> affiche un msg d'erreur
    -> on repose la question
3. return le choix de l'utilisateur

#### function get_computer_item(self)

1. cree une liste des choix possible possibilities = ["r", "p", "s"]
2. on utilise random choice pour choisir au hasard
3. return le choix

##### function get_game_result(self, user_item, computer_item)

-> condition -> etablir quel choix est le plus fort
-> return le resultat

##### function play(self)
1. j'appelle get_user_item pour recuperer le user_choice
    `user_choice = self.get_user_item()`
2. j'appelle get_computer_item pour recuperer le computer_choice
    `computer_choice = self.get_computer_item()`
3. j'appelle get_game_result pour recuperer le resultat
    `resultat = self.get_game_result(user_choice, computer_choice)`
4. j'affiche le resultat dans une phrase "tu as gagne ce jeux"...
5. return "win", soit "loss", soit "draw" -> return `resultat`


### rock-paper-scissors.py

##### function get_user_menu_choice()

1. input pour poser la question si la personne veut (g) ou pas jouer (x)
2. tant que l'utilisateur ne me donne pas soit g doit x, on continue de lui poser la question
3. return le choix de l'utilisateur soit (g) soit (x)

##### function print_results(results)  #  {win: 2,loss: 4,draw: 3}

-> print "Voici tes resultats"
-> boucler sur les valeurs
    "you won 2 times"
    "you lost 4 times" ...

#### function main()

Attention le faut importer l'autre fichier (game.py)

1. creer un dictionnaire qui va sauvegarder mes resultats

`all_results = {"win" : 0, "loss" : 0, "draw": 0}`

1. Verifier si l'utilisateur veur jouer
    `do_we play = get_user_menu_choice()`

    -> tant que le do_we play == "g" : DANS LA BOUCLE WHILE

    1.1. Si il veut jouer, je cree un objet de la classe Game
        `game = Game()`
        `game_result = game.play()` la variable game_result est egale a la valeur renvoyee par la fonction play

        exemple :
        `game_result = "win"`
        `game_result = "loss"`
        `game_result = "draw"`

        `all_results[game_result] += 1` j'utilise la chaine de caractere comme une clef de mon dictionnaire

        `do_we play = get_user_menu_choice()`

2. A L'EXTERIEUR LA BOUCLE WHILE (la personne ne veut plus jouer)

    `print_results(all_results)`


--> ENFIN : j'appelle la fonction `main()` pour executer toute la logique


```
n = 1

while do_we_play == "g" :
   -> je le fais jouer
    -> je sauvegarde les resultat
    -> je lui pose la question

```