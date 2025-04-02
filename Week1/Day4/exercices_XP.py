# Exercice 1:
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Réponses aux questions ############################################################   

class Siamese(Cat):
    def __init__(self, name, age, eyes_color = "blue"):
       super().__init__(name, age)
       

cat_1 = Bengal("Felix", 3)
cat_2 = Chartreux("Mimi", 5)
cat_3 = Siamese("Melo", 2)
all_cats = [cat_1, cat_2, cat_3 ]

sara_pets = Pets(all_cats)

sara_pets.walk()

#Exercice2 : 
class Dog():
    def __init__(self, dog_name, dog_age, dog_weight):
        self.age = dog_age
        self.name = dog_name
        self.weight = dog_weight
     
    def bark(self):
        print(f"The dog {self.name} aboie")

    def run_speed(self):
        return self.weight / self.age*10

    def fight(self, other_dog):
        if self.run_speed() * self.weight >  other_dog.run_speed() * other_dog.weight:
            return f"{self.name} a remporté le combat contre {other_dog.name}"
        else:
             return f"{other_dog.name} a remporté le combat contre {self.name}"

dog_1 = Dog("Rex", 5, 30)
dog_2 = Dog("Max", 4, 35)
dog_3 = Dog("Felix", 3, 28)

dog_1.bark()
dog_2.bark()
dog_3.bark()

print(dog_1.fight(dog_2))
print(dog_1.fight(dog_3))
print(dog_2.fight(dog_3))



# Exercice 3:===> see file exo3.py

# Exercice 4 : 
class Family:
    def __init__(self, fam_members, fam_lname):
        self.members = fam_members  # Initialisation de la liste des membres
        self.last_name = fam_lname
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulation! {kwargs['name']} is born in {self.last_name} family!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] > 18:
                    return True
        return False

    def family_presentation(self):
        print(f"Famille {self.last_name} :")
        for member in self.members:
            print(f"  - {member['name']}, {member['age']} ans")

# Création d'une instance de Family
fam_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
Fam = Family(fam_members, "Dupont")
Fam.born(**{"name": "Dody", "age": 0, "gender": "Male", "is_child": True})
print(Fam.is_18("Michael"))  


#Exercice 5:
class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(f"{member['name']} utilise son pouvoir : {member['power']}")
                    return
                else:
                    raise Exception(f"{member['name']} n'a pas encore 18 ans !")
        raise Exception(f"{name} n'est pas un membre de la famille.")

    def incredible_presentation(self):
        print("* Here is our powerful family **")
        super().family_presentation()  # Appelle la méthode de la classe parente




# Création d'une instance de TheIncredibles
incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]
incredibles_family = TheIncredibles(incredibles_members, "Incredibles")

incredibles_family.incredible_presentation()
incredibles_family.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')


incredibles_family.incredible_presentation()

# Utilisation du pouvoir d'un membre
try:
    incredibles_family.use_power('Michael')
    incredibles_family.use_power('Jack')     
except Exception as e:
    print(e)
