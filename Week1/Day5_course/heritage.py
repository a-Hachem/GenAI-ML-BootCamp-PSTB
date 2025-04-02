
# classe mere
class Dog :
    def __init__(self, name_dog, age_dog) :
        self.name = name_dog
        self.age = age_dog
        self.race = "Yorkshire"
        self.energy = 5 #HEURES

    def play(self, tool):
        if tool == "balle" :
            self.energy -= 0.5
        elif tool == "baton" : 
             self.energy -= 1
        elif tool == "master" : 
            self.energy -= 2
        else :
            self.energy -= 4
    
    def bark (self) :
        print("OUAF OUAF")

    def smile(self):
        print("je sourisss")

# class fille, qui herite de la classe mere qui est Dog
class Old_Dog(Dog):

    def __init__(self, name, age, color):
        super().__init__(name, age) ##appelle la fonction init() de la classe mere
        self.pelage = color #je cree un attribut pour le vieux chien
        self.energy = 2 #je change l'attribut 
        

    def bark(self) : #meme nom que la fonction de la classe mere
        super().bark() #appelle la fonction bark() de la classe mere
        super().smile() #le classe old dog herite de dog, doc automatiquement elle a la fonction smile
        print("je suis vieux")

dog_1 = Old_Dog("Miky", 10, "grey") 
print(dog_1.name)
print(dog_1.energy)

# dog_1 = Old_Dog("Miky", 10) #object de la classe Old_dog = #instance de la classe Old_dog
# print(dog_1.race) # Yorkshire #attribut de la classe mere
# print(dog_1.name) # Miky

# dog_1.bark()

# dog_2 = Dog("Lola", 1)
# dog_2.bark()