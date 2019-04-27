class Employee:

    salary = 0

    def __init__(self, name, professional_level, base_pay, hours_worked):
        self.name = name
        self.professional_level = professional_level
        self.base_pay = base_pay
        self.hours_worked = hours_worked

    def check(self):
        if self.base_pay < 8:
            print("Error \n")
            return False
        else:
            if self.hours_worked > 40:
                salary = self.hours_worked * self.hours_worked
                salary = salary + (self.hours_worked-40) * self.base_pay * 0.5
                print("Good Overtime. The salary is ", salary)
            else:
                salary = self.hours_worked * self.hours_worked
                print("The salary is ", salary)
            return True

    def salary(self):
        salary = self.base_pay*self.hours_worked
        print("Total salary for "+self.name+" is "+str(salary)+" dollar")

    def office(self):
        if self.professional_level == "A":
            print(self.name, "has an individual office room \n")
        elif self.professional_level == "B":
            print(self.name, "has a cubicle room \n")


class Manager(Employee):
    def __init__(self, name, professional_level, base_pay, hours_worked, office_number):
        Employee.__init__(self, name, professional_level, base_pay, hours_worked)
        self.officeNumber = office_number

    def office_number(self):
       if self.professional_level == "A":
           print("Manager " + self.name + " has an individual office room in", self.officeNumber)
       elif self.professional_level == "B":
           print(self.name, "has a cubicle room \n")


name = ["John", "Graham", "Annabel", "Margaret"]
professional_level = ["B", "B", "A", "B"]
base_pay = {8.50, 9.00, 9.20, 7.80}
hours_worked = [35, 37, 43, 45]
name_manager = ["Bill", "Gregory"]
professional_level_manager = ["A", "A"]
base_pay_manager = [15.00, 16.50]
hours_worked_manager = [49, 47]
office_number = ["A332", "A415"]

employee_list =[]
manager_list=[]

for x in range(len(name)):
    employee_list.append(Employee(name[x], professional_level[x], base_pay[x], hours_worked[i]))

for x in range(len(name_manager)):
    manager_list.append(Manager(name[x], professional_level[x], base_pay[x], hours_worked[i], office_number[i]))

for x in range(len(name)):
    print("The employee name is " + employee_list[i].name)
    if employee_list[i].check():
        employee_list[i].salary()
        employee_list[i].office()

for x in range(len(name_manager)):
    print("The manager name is " + manager_list[i].name)
    if manager_list[i].check():
        manager_list[i].salary()
        manager_list[i].office_number()

    # for (int i=0; i < nameManager.length;i++) {
    #     System.out.println("The manager name is " + managerList.get(i).name);
    # if (managerList.get(i).check()) {
    # managerList.get(i).salary();
    # managerList.get(i).hasOffice();
    # }
    # }

# John = Employee("John", "B", 7.5, 38)
# John.check()
# John.salary()
# John.office()
#
# John = Manager("John", "A", 7.5, 38, "A415")
# John.salary()
# John.office()
# John.office_number()




