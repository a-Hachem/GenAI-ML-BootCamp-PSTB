class Farm :
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
        # self.all_animals = []

    def add_animal(self, animal_name, animal_number = 1) :
        if animal_name in self.animals :
            self.animals[animal_name] += animal_number #increment
        else :
            self.animals[animal_name] = animal_number #creation
            # self.all_animals.append(animal_name) #ajout dans la liste

    def get_info(self):
        message = f"{self.name} Farm \n \n"
        for animal, number in self.animals.items() :
            message += f"{animal} : {number} \n"
        message += "\n \t E-I-E-I-0!"
        return message
    
    def get_animal_types(self):
        # return sorted(self.all_animals)
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        all_animals_sorted = self.get_animal_types()
        list_animals = []
        for animal in all_animals_sorted :
            if self.animals[animal] > 1 :
                list_animals.append(f"{animal}s")
            else :
                list_animals.append(f"{animal}")
            # ["cows", "sheeps", "rabbits"]
            message = f"{self.name} Farm has {", ".join(list_animals[:-1])} and {list_animals[-1]}"
        return message

# quels attributs
# quelles methodes
    # besoin de parametres ?
    # besoin de renvoyer? retourner ?

# objet = instance de la class Farm
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
# print(f"voici mes animaux {macdonald.animals}")
macdonald.add_animal('cow',2)
# print(f"voici mes animaux {macdonald.animals}")
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('rabbit', 3)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
# print(f"voici mes animaux {macdonald.animals}")



# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# ------------
# default argument
# def check_user (first_name, age = 1) :
#     print(f"{first_name} is {age} years old")

# check_user("John", 30)
# check_user("Lea")
# ------------

# IF IN
# colors = ["blue", "red", "yellow"]
# if "yellow" in colors :
#     print("SUPER")

# if "green" in colors :
#     print("SUPER")
# else :
#     print("NO")

# if "green" not in colors :
#     print("SUPER")
# ------------


# list
# colors = ["blue", "red", "yellow"]
# print(colors[1:3]) #1 a 3 non inclu
# print(colors[0:2]) #0 a 2 non inclu
# print(colors[:2]) #0 a 2 non inclu
# print(colors[:-1]) #0 au dernier non inclu