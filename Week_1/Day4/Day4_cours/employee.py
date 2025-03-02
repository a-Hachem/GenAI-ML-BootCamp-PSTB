class Employee :

    # class attributes
    company = "Amazon"
    number_employees = 0

    def __init__(self, fn, ln, age_emp, job_emp, salary_emp) :
        self.first_name = fn
        self.last_name = ln
        self.age = age_emp
        self.job = job_emp
        self.salary = salary_emp
        Employee.number_employees += 1 # des qu'un objet est cree, on augmente le "class attribute"
        Employee.welcome()

    def full_name(self) :
        return self.first_name + " " + self.last_name
    
    def happy_birthday(self) :
        self.age += 1
        return self.age
    
    def get_promotion(self, amount):
        self.salary += amount

    def show_info(self):
        print(f"The employee named {self.full_name()} is {self.age} years old, he is a {self.job}, she/he earns {self.salary} euros")

    # methode statique
    # methode qui ne prend pas le parametre self
    # mais vous voulez quand meme qu'elle doit dans la classe
    # decorateur
    @staticmethod
    def welcome():
        print("WELCOME")

    @classmethod #method auquelle on accede avec la classe
    def detail_class(cls, fn, ln, age_emp, job_emp, salary_emp):
        cls.company = "Apple"
        cls(fn, ln, age_emp, job_emp, salary_emp)
    
    @classmethod
    def special_employee(cls, fn, ln, age_emp, job_emp, salary_emp):
        if age_emp >= 18 :
            new_obj = cls(fn, ln, age_emp, job_emp, salary_emp)
            new_obj.show_info()
        else :
            print("You are too young to work")


# employee_1 = Employee("Angelina", "Jolie", 23, "secretary", 400)

# Employee.detail_class("Angelina", "Jolie", 23, "secretary", 400)
# Employee.welcome() # classe
Employee.special_employee("Angelina", "Jolie", 23, "secretary", 400)

