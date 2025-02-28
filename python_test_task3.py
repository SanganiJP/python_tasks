class Employee:
    def __init__(self):
        self.employees = [{'emp_name':'Jayesh','employee_id':1,'salary':10000,'role':'Developer','extra_info':{'Dept_name':'Development','p_language':'java'}},
        {'emp_name':'Sanket', 'employee_id': 2, 'salary': 20000, 'role': 'Manager', 'extra_info': {'Dept_name': 'Development', 'p_language': 'java'}}
        ]

    def employee_creation(self):
        emp_roles = ["Developer","Manager"]
        n = int(input("Enter the number of employees."))
        for i in range(n):
            emp_info = {}
            employee_id = int(input("Enter employee_id:"))
            emp_info["employee_id"] = employee_id
            emp_name = input("Enter name:")
            emp_info["emp_name"] = emp_name
            salary = input("Enter salary:")
            emp_info["salary"] = salary
            role = input("Enter role:")
            emp_info["role"] = role
            self.employees.append(emp_info)

    def display_all_employees(self):
        for emp in self.employees:
            employee_id = emp.get('employee_id')
            emp_name = emp.get('emp_name')
            print(f'employee_id:{employee_id} Employee Name:{emp_name}')

    def filter_by_role(self):
        emp_role = input("Enter employee role that you want to find:")
        for emp in self.employees:
            print(f"Employee role:{emp_role}")
            if emp.get('role') == emp_role:
                employee_id = emp.get('employee_id')
                emp_name = emp.get('emp_name')
                print(f'employee_id:{employee_id} Employee Name:{emp_name}')

    def filter_by_salary(self):
        min_salary = int(input("Enter starting salary from:"))
        max_salary = int(input("Enter salary end from::"))
        for emp in self.employees:
            if emp.get("salary")>min_salary and emp.get("salary")<max_salary:
                employee_id = emp.get('employee_id')
                emp_name = emp.get('emp_name')
                salary = emp.get('salary')
                print(f'employee_id:{employee_id} Employee_Name:{emp_name} Salary:{salary}')

e1 = Employee()

while True:
    print("Choice:")
    print("1.Show All employee")
    print("2.Filter employee by salary range")
    print("3.Filter employee by role")
    print("4.Employee creation")
    print("5.Exit")

    try:
        choice = int(input("Enter task choice that you want to perform:"))
        match choice:
            case 1:
                e1.display_all_employees()
            case 2:
                e1.filter_by_salary()
            case 3:
                e1.filter_by_role()
            case 4:
                e1.employee_creation()
            case _:
                print("Enter valid choice!")
    except Exception as e:
        print(e)



