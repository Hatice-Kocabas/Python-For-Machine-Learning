class HealthInsurance:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, num_of_employees, num_of_clients):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.num_of_employees = num_of_employees
        self.num_of_clients = num_of_clients

    def print_report(self):
        print(f""" The company {self.company_name} was founded in {self.foundation_year}.
        The founder of the company is {self.founder_name}.
        Company Slogan: {self.company_slogan}.
        number of employee: {self.num_of_employees}
        number of clients: {self.num_of_clients}
        """)

    def sup_health_insurance(self, age, chronic_disease, income):
        if age >= 60 and chronic_disease == True and income < 6000:
            print("We are sorry! You are not eligible for supplemental health insurance.")
        elif age < 60 and income >= 6000 or chronic_disease == False:
            print("Congratulations.You can get supplemental health insurance.")

    def update_num_clients(self, new_number):
        self.num_of_clients = new_number
        print(
            f"The number of clients has been changed to {self.num_of_clients}!")


HI_Company = HealthInsurance(
    "Healthy", 2012, "Bob Mayer", "We car for you", 3500, 13230,)
HI_Company.sup_health_insurance(45, False, 5000)
HI_Company.update_num_clients(13231)
HI_Company.print_report()
