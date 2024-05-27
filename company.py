from employee import Employee
class Company:
    def __init__(self):
        self.employees = []

    def addEmployee(self, newEmployee):
        self.employees.append(newEmployee)

    def displayEmployeeAndPayCheck(self):
        print('Current Employees and their Paycheck:')
        for i in self.employees:          
            print(i.fname, 'Paycheck ' f'Amount: ${i.calculate_weeklyPaycheck():,.2f}')            
        print('End of Employee List.....')


def main():
    myCompany = Company()
    employee1 = Employee('Ananda', 'Chandran', 5000)
    employee2 = Employee('Vijay', 'Prakash', 5000)
    myCompany.addEmployee(employee1)
    myCompany.addEmployee(employee2)
    myCompany.displayEmployeeAndPayCheck()
    # for i in myCompany.employees:
    #     print(i.fname)    
main()
    