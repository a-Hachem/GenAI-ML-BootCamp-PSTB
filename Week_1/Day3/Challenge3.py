class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        # Dictionary to store animals and their counts
        self.animals = {}
    
    def add_animal(self, animal_name, num_animal=1):
        # If the animal already exists in the dictionary, increment its count
        if animal_name in self.animals:
            self.animals[animal_name] += num_animal
        # Otherwise, add the animal to the dictionary with the given count
        else:
            self.animals[animal_name] = num_animal

    def get_info(self):
        # Start building the info string with the farm name
        info = f"{self.name}'s farm\n\n"
        
        # Loop through the dictionary to add each animal and its count to the info string
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        
        # Add the final line with "E-I-E-I-0!"
        info += "\n    E-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        # Return a sorted list of animal types (keys of the dictionary)
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        # Get a sorted list of animal types using the get_animal_types method
        animals = self.get_animal_types()

        # Create a list to store animal names with proper pluralization
        animals_with_plural = []
        for animal in animals:
            # If there is more than one animal of this type, add an "s" to the name
            if self.animals[animal] > 1:
                animals_with_plural.append(animal + "s")  # Add "s" for plural
            # Otherwise, keep the name as is (singular)
            else:
                animals_with_plural.append(animal)  # Keep singular form

        # Format the final phrase based on the number of animal types
        if len(animals_with_plural) == 1:
            # If there is only one animal type, use a simple sentence
            phrase = f"{self.name}'s farm has {animals_with_plural[0]}."
        else:
            # If there are multiple animal types, join them with commas and "and"
            animals_str = ", ".join(animals_with_plural[:-1])  # Join all but the last animal with commas
            animals_str += f" and {animals_with_plural[-1]}"  # Add the last animal with "and"
            phrase = f"{self.name}'s farm has {animals_str}."

        return phrase


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Print the detailed farm information
print(macdonald.get_info())

# Print the short farm information
print(macdonald.get_short_info())