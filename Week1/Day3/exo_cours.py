class Employee :
    # Si l'on veut que tousles employees soient chez amazon 
    compagny = "Amazon"  # ça peut servir si on veut savoir le nombre d'emplyés créés
    number_employee =0
    def __init__(self, first_name, last_name, user_age, user_job, user_salary ):
        self.firstname = first_name
        self.lastname = last_name
        self.age = user_age
        self.job = user_job
        self.salary = user_salary
        Employee.number_employee +=1     # des qu'un objet est creer, number empleyee est increment de 1

        def fullname(self):
            user_fullname = self.first_name + ""+ self.user_name
            return(user_fullname)
        
        def happy_birthday(self):
            birthday = self.age + 1             # ou bien self.age +=1   return(self.age)
            return(birthday)
        
        def get_promotion(self, amount):
            self.salary += amount
            return(self.salary)
        
        def show_infos(self):
            print(f"The employee named {self.fullname()} is {self.age()} years old, he is {self.job()} ")
        
employee_1 = Employee("Lea", "Smith", 30, "Developper", 20000)
#employee_1 est bojet de la classe Emlpoyee = instance de la classe
employee_2 = Employee("John", "Vik", 19, "Data analyst", 40000)

employee_1.get_promotion(10000)
employee_1.show_birthday()

