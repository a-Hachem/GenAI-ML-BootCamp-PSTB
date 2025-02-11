# Exercie 1:
#Convert the two following lists, into dictionaries.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

# Exercie 2:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def ticket_price(age):
    ticket = 0
    if age < 3:
        ticket = 0
    elif age >= 3 and age <=12:
        ticket = 10
    else: 
        ticket = 15
    return ticket
#ON affiche le prix de chaque membre de la famille en appelant la fonction ticket_price
for name, age in family.items():
    print(f"{name} will pay {ticket_price(age)}")

total_cost = sum(ticket_price(age) for age in family.values())
print(f"The family will pay {total_cost} € for the movies")

# Bonus

family = {}

while True:
    name_age = input("Enter the name of a person and their age (or type 'stop' to finish): ")

    if name_age.lower() == "stop":
        break  # Stoper la boucle
    name, age = name_age.split()
    family[name] = int(age)  # Ajoute l'entrée donnée au dictionnaire
    print(family)  # Affiche le dictionnaire mis à jour

    
# Exercie 4:
def describe_city(city, country="France"):
    print(f"The city of {city} is in {country}")

describe_city("Paris")

# Exercie 8:
data = [
        {
        "question": "What is Baby Yoda's real name?", 
         "answer": "Grogu"
         },
        {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
        },
        {
         "question": "What year did the first Star Wars movie come out?",
          "answer": "1977"
        },
        {
        "question": "Who built C-3PO?", 
        "answer": "Anakin Skywalker"
        },
        {
        "question": "Anakin Skywalker grew up to be who?", 
        "answer": "Darth Vader"
        },
        {
        "question": "What species is Chewbacca?", 
        "answer": "Wookiee"
        }
    ]
def quiz_list():
    correct_answers = 0
    incorrect_answers = 0
    incorrect_list = []  # Stocke les erreurs
    
    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was: {item['answer']}\n")
            incorrect_answers += 1
            incorrect_list.append((item["question"], user_answer, item["answer"]))
    return correct_answers, incorrect_answers, incorrect_list

def show_results(correct, incorrect, incorrect_list):
    print(f"\n Quiz Results ")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

    if incorrect > 0:
        for question, user_ans, correct_ans in incorrect_list:
            print(f"- {question}")
            print(f" Your answer: {user_ans}")
            print(f" Correct answer: {correct_ans}\n")

# Lancer le quiz et afficher les résultats
correct, incorrect, incorrect_list = quiz_list()
show_results(correct, incorrect, incorrect_list)

    

