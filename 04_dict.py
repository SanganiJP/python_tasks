
student = {"Name" : "Jayesh","city" : "Bhavnagar","marks" : 90}
marks = {'p':90,'c':93,'m':98}
student["SPI"] = 8.0
t_marks = {}

student["city"] = "Mahuva"
for sub,mark in marks.items():
    t_marks[sub] = 10 + mark

if "Name" in student:
    student["Name"] = "Sanket"

student.update({"roll_no":40 ,"profession":"B.E"})
# print(student)
print(t_marks)
#remove item of dictionary using key
# student.pop("roll_no")
# student.pop("profession")
#remove last item of dictionary using popitem()
#student.popitem()

#to delete item of dictionary using key
#del student["Name"]
# del student
#method clear the dictionary
# student.clear()
print(student)
for key, val in student.items():
    print(f"{key} : {val}")

