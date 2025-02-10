# %%
import random

# %%
def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7
    for attempt in range(max_attempts):
        num_gamer = int(input(f"It's your {attempt}/{max_attempts}, Enter a number: "))
        if num_gamer < random_number:
            print("Too low!")
        elif num_gamer > random_number:
            print("Too high!")
        else: 
            print(f"Congratulations! You are the winner !" )
            break
    else:
        print(f"The number was {random_number}, good luck for next game ! ")
    

# %%
number_guessing_game()