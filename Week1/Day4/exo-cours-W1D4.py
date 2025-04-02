class Employee() :

    company = "Amazon"
    number_employees = 0

    def __init__(self, fn, ln, age_emp, job_emp, salary_emp) :
        self.first_name = fn
        self.last_name = ln
        self.age = age_emp
        self.job = job_emp
        self.salary = salary_emp
        Employee.number_employees += 1 # des qu'un objet est cree, onaugmente le "class attribute"

    def full_name(self) :
        return self.first_name + " " + self.last_name
    
    def happy_birthday(self) :
        self.age += 1
        return self.age
    
    def get_promotion(self, amount):
        self.salary += amount

    def show_info(self):
        print(f"The employee named {self.full_name()} is {self.age} years old, he is a {self.job}, she/he earns {self.salary} euros")

employee_1 = Employee("Lea", "Smith", 30, "developer", 20000)
#employee_1 c'est un objet de la classe Employee
#employee_1 c'est une instance de la classe Employee

employee_2 = Employee("John", "Vik", 19, "data analyst", 40000)

# employee_1.get_promotion(10000)
# employee_1.show_info()
# employee_1.happy_birthday()
# employee_1.show_info()

# employee_2.show_info()

print(employee_1.company)
print(Employee.company)

print(Employee.number_employees)

class Developer(Employee):
     def __init__(self, fn, ln, age_emp, job_emp = "developer"  salary_emp =15000):
        super().__init__(fn, ln, age_emp, job_emp, salary_emp)
        self.coding_skills = []

        def add_skills(self, *skills) : 
            #receives a tuple of skills and append them to the coding skills list
            return self.coding_skills.extend(skills)

        def coding(self) : 
            #print a nice sentence with all the coding languages the developer knows
            print(f"The developer {self.firstname} {self.lastname} has tihs skills {self.a}")

        def coding_with_partner(self, other_developer) : 
            #print a nice sentence with the name of both developers, and their skills
            list_dev = [....]
            for dev in list_dev:
                print{f"{self.firstname} {self.lastname} has tihs skills {self.add_skills}"}


dev_1 = Developer("Tom", "Cruiz", 30)
dev_2 = Developer("Angelina", "al", 23) 

dev_1. 