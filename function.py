def update_student(std_Name,std_Age,std_School,std_city,std_fees = 20000):
    std_details = {
        'std_Name':std_Name,
        'std_Age':std_Age,
        'std_School':std_School,
        'std_fees':std_fees,
        'std_city':std_city
    }
    return std_details

def count_std_city(students_data):
    std_count = {}
    for std in students_data:
        city_name = std['std_city']
        if std_count.get(city_name):
            std_count[city_name] += 1
        else:
            std_count[city_name] = 1
    return std_count

def change_school(students_data):
    for student in students_data:
        if student.get('std_School') == 'vdvs':
            student['std_School'] = 'GM'

def count_std_school_wise(students_data):
    no_of_std_inSchool = {}
    for student in students_data:
        school_name = student['std_School']
        if no_of_std_inSchool.get(school_name):
            no_of_std_inSchool[school_name] += 1
        else:
            no_of_std_inSchool[school_name] = 1
    return no_of_std_inSchool


students_data = []
is_need = True
while is_need:
    std_Name = input("Enter student name:")
    std_Age = input("Enter your age:")
    std_School = input("Enter your school name:")
    std_fees = input("Enter your school fees:")
    std_city = input("Enter your city name:")

    sd = update_student(std_Name=std_Name, std_Age=std_Age, std_School=std_School, std_fees=std_fees, std_city=std_city)
    students_data.append(sd)

    is_stop = input('Do you want to stop?y/n:')
    if is_stop.lower() == 'y':
        is_need = False

print(students_data)
change_school(students_data)
print(students_data)

noOfStudentInSchool = count_std_school_wise(students_data)
print(noOfStudentInSchool)

count_std = count_std_city(students_data)
print(count_std)

