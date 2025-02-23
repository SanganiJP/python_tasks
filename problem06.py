def total_marks(students):
    """
    This function return student with their total marks that we are stored at result dictionary
    This function return student with their average marks that we are stored at avg_marks dictionary
    """
    result = {}
    total_exam = {}
    avg_marks = {}
    for key,val in students.items():
        name = key.split("-")[0]
        if result.get(name):
            result[name] += val
            total_exam[name] += 1
            avg_marks[name] = round(result[name]/total_exam[name],2)
        else:
            result[name] = val
            total_exam[name] = 1
            avg_marks[name] = val
    return result,avg_marks

def max_mark_per_sub(students):
    """
    this function return dictionary where we store subject with highest marks
    """
    maxmarkpersub = {}
    # max_markpersub = {}
    # for key,v in students.items():
    #     student,subject = key.split("-")
    #     if subject in max_markpersub:
    #         if max_markpersub[subject][1]<v:
    #             max_markpersub[subject] = (student,v)
    #     else:
    #         max_markpersub[subject] = (student,v)

    std = {}
    for key,val in students.items():
        student = key.split("-")[0]
        subject = key.split("-")[1]
        if maxmarkpersub.get(subject):
            maxMark = maxmarkpersub[subject]
            if maxMark < val:
                maxmarkpersub[subject] = val
                std.pop(subject)
                std[subject] = student,val
        else:
            maxmarkpersub[subject] = val
            std[subject] = student,val
    return std,maxmarkpersub

def find_max(total_marks):
    """
    This function iterate through total_marks dictionary and return
    highest scorer student name and mark
    """
    stdudent = max(total_marks.items(), key=lambda i: i[1])[0]
    maxmark = max(total_marks.items(), key=lambda i: i[1])[1]
    return stdudent,maxmark

def std_dict(total_marks):
    sorted_dict_desc = dict(sorted(total_marks.items(), key = lambda i:i[1], reverse=True))
    return sorted_dict_desc

students = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}
total_marks,avg_marks = total_marks(students)
print(f'Task 1: Total marks obtain by students : {total_marks}')
print(f'Task 2: Average Marks of Students : {avg_marks}')
high_scorer_std,mark = find_max(total_marks)
print(f'Task 3: Student has the highest total marks:- Name:{high_scorer_std},obtain Marks:{mark}')
std,sub_mark = max_mark_per_sub(students)
print(f'Task 4: Subject-wise Highest Marks : {sub_mark}')
print(f'Task 5: Subject-wise Highest Marks with student name : {std}')
# print(f'Task 5: Sorted Dictionary:{std_dict(total_marks)}')


