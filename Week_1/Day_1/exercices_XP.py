# Exercice 1:
print("Hello world\n" * 4, end="")

# Exercice 2:
result = (99 ** 3) * 8
print(result)


# Exercice 3:
user_name = input("Enter your name: ")
my_name = "Aïcha"
if user_name.lower() == my_name.lower():
    print(f"Wow! We have the same name! nice to meet you")
else: 
    print(f"Nice to meet you {user_name}, my name is {my_name}.")


# Exercice 4:

user_height = int(input("Enter your height in cm: "))
if user_height > 145:
    print("Ok! You're tall enough, you can get on board! ")
else:
    print("Sorry, you need to grow a little more before you're allowed to board.")


# Exercice 5:
my_fav_numbers = {2, 8, 11, 12, 17, 18}
two_numbers = {9, 29}
my_fav_numbers.update(two_numbers)
my_fav_numbers.remove(29)
friend_fav_numbers = {1, 3, 5, 7, 11}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(f"My favorite numbers: {our_fav_numbers}")


# Exercice 6:

# A tuple is immuable, which means we cannot add new integers to it. 

# Exercice 7:
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
print(f"The are {apple_count} apples in the basket")
basket.clear()
print(basket)


# Exercice 8:
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
                   "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  # Retirer le premier sandwich de la liste
    finished_sandwiches.append(sandwich)  # L'ajouter à la liste des sandwichs terminés
    
for sandwich in finished_sandwiches:
    print(f"- I made your {sandwich}")

