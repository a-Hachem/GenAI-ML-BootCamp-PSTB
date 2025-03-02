from employee import Employee

# #INHERITANCE
class Developer(Employee) :
    def __init__(self, fn, ln, age_emp, job_emp = "developer", salary_emp = 15000):
        super().__init__(fn, ln, age_emp, job_emp, salary_emp) #j'appelle l'init de parent cad la classe employee
        self.coding_skills = []

    def add_skills(self, *skills): #*args = tuple
        self.coding_skills.extend(skills)

    def coding(self) :
        print(f"{self.first_name} knows the languages {self.coding_skills}")

    def coding_with_partner(self, other_developer) :
        print(f"{self.first_name} works with {other_developer.first_name}")
    
    def get_promotion(self, amount): #ecraser la methode get_promotion de l'employee
        self.salary *= amount

    def __add__(self, other_developer) :
        return self.coding_skills + other_developer.coding_skills
    
    def __eq__(self, other_developer):
        return self.job == other_developer.job

developer_1 = Developer("Tom", "Cruz", 30)
developer_2 = Developer("Angelina", "Jolie", 23)
employee_1 = Employee("Angelina", "Jolie", 23, "secretary", 400)
developer_1.add_skills("python", "sql")
developer_1.add_skills("javascript", "excel")
print(developer_1 + developer_2) # appele __add__ dunder method
# print(developer_1.coding_skills.__add__(developer_2.coding_skills)) # meme
print(developer_1 == developer_2) # True
print(developer_1 == employee_1) # False


# print(developer_1.first_name)
# print(developer_1.full_name())
# developer_1.add_skills("python", "sql")
# print(developer_1.coding_skills)
# developer_1.coding()
# developer_1.coding_with_partner(developer_2)
# developer_1.get_promotion(1000)

# developer_1.show_info()


