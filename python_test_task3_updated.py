class Employee:
    def __init__(self):
        """Initialize the employee list."""
        self.employees = []

    def employee_creation(self):
        """Create new employee records and store them in the list."""
        n = int(input("Enter the number of employees:"))
        for i in range(n):
            emp_info = {}
            emp_info["employee_id"] = int(input("Enter employee_id:"))
            emp_info["emp_name"] = input("Enter name:")
            emp_info["salary"] = int(input("Enter salary:"))
            emp_role = input("Enter role:")
            if emp_role not in ["Developer","Manager"]:
                print("This role is not valid!")
                continue
            else:
                emp_info["role"] = emp_role
                if emp_role == "Developer":
                    emp_info["extra_info"] = input(f"Enter programming language:")
                else:
                    emp_info["extra_info"] = input(f"Enter department of Manager:")
            self.employees.append(emp_info)
            print(f"Employee detail added successfully!!")

    def display_all_employees(self):
        """Display details of all employees in the list."""
        flag = True
        for emp in self.employees:
            print(emp)
            flag = False
        if flag:
            print("Employees not found!")

    def filter_by_role(self):
        """Filter and display employees based on their role."""
        emp_role = input("Enter employee role that you want to find:")
        flag = True
        for emp in self.employees:
            if emp.get('role') == emp_role:
                employee_id = emp.get('employee_id')
                emp_name = emp.get('emp_name')
                print(f'employee_id:{employee_id} Employee Name:{emp_name}')
                flag = False
        if flag:
            print(f"This {emp_role} of employee not exist!")


    def filter_by_salary(self):
        """Filter and display employees within a salary range."""
        min_salary = int(input("Enter starting salary from:"))
        max_salary = int(input("Enter salary end from::"))
        flag = True
        for emp in self.employees:
            if min_salary <= emp.get("salary") <= max_salary:
                employee_id = emp.get('employee_id')
                emp_name = emp.get('emp_name')
                salary = emp.get('salary')
                print(f'Employee_Name:{emp_name} Salary:{salary}')
                flag = False
        if flag:
            print("Not a single employee found in this salary range!")



def quit_continue():
    inp = input("Do you want continue with EMS Y/N?")
    if inp.lower() == "y":
        perform_op()
    else:
        exit()

def perform_op():
    """Display menu and execute user-selected employee operations."""
    e1 = Employee()
    while True:
        print("Choice:")
        print("1.Show All employee")
        print("2.Filter employee by salary range")
        print("3.Filter employee by role")
        print("4.Employee creation")
        print("5.Quite EMS")

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
                case 5:
                    break
                case _:
                    print("Enter valid choice!")
            quit_continue()
        except Exception as e:
            print(f'Error:{e}')
            print("Please enter valid choice!")
            quit_continue()

print("Employee Management System")
quit_continue()



