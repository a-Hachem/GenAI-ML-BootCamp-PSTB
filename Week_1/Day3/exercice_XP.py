# # Exercice 1:
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat_1 = Cat("mimi", 2)
# cat_2 = Cat("nemo", 1)
# cat_3 = Cat("wistiti", 6)
# #print(f"The cat {cat_1.name} is {cat_1.age} older")

# def find_oldest_cat(cat_1, cat_2, cat_3):
#     oldest_cat = max([cat_1, cat_2, cat_3], key= lambda cat : cat.age)
#     return oldest_cat

# oldest = find_oldest_cat(cat_1, cat_2, cat_3)
# print(f"The oldest cat is {oldest.name} and is {oldest.age} years old")

# # Exercice 2:
# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         print(f"{self.name} jumps {int(self.height)*2} cm height!")

# davids_dog = Dog("Rex", 50)
# print(f"{davids_dog.name} can height until {davids_dog.height}")
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(f"{sarahs_dog.name} can height until {sarahs_dog.height}")
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is the bigger dog")
# else: 
#     print(f"{sarahs_dog.name} is the bigger dog")


# # Exercice 3:
# class Song:
#     def __init__(self, lyrics_song):
#         self.lyrics = lyrics_song

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# Exercice 4:

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
           self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            
    def group_animals(self):
        sorted_animals = sorted(self.animals, key=lambda animal: animal[0].lower())
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)

        return grouped_animals

    
    def get_groups(self):
        grouped_animals = self.group_animals()  
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")


safari = Zoo("ramat_gan_safari")
safari.add_animal("Giraffe")
safari.add_animal("Lion")
safari.add_animal("Champanzee")
safari.get_animals()    
safari.sell_animal("Lion")
safari.group_animals()
safari.get_groups()